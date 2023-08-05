"""
Semi-random access to bz2 compressed data.
"""

import bisect
import os
from io import BytesIO
import sys

from six import Iterator

try:
    import pkg_resources
    pkg_resources.require( 'python_lzo' )
    import lzo
except:
    pass

import struct

from bx_extras import lrucache   
    
class SeekableLzopFile( Iterator ):
    """
    Filelike object supporting read-only semi-random access to bz2 compressed
    files for which an offset table (bz2t) has been generated by `bzip-table`.
    """
    
    def __init__( self, filename, table_filename, block_cache_size=0, **kwargs ):
        self.filename = filename
        self.table_filename = table_filename
        self.init_table()
        self.file = open( self.filename, "rb" )
        self.dirty = True
        self.at_eof = False
        self.file_pos = 0
        self.current_block_index = -1
        self.current_block = None
        if block_cache_size > 0:
            self.cache = lrucache.LRUCache( block_cache_size )
        else:
            self.cache = None
        
    def init_table( self ):
        self.block_size = None
        self.block_info = []
        # Position of corresponding block in compressed file (in bytes)
        for line in open( self.table_filename ):
            fields = line.split()
            if fields[0] == "s":
                self.block_size = int( fields[1] )
            if fields[0] == "o":
                offset = int( fields[1] )
                compressed_size = int( fields[2] )
                size = int( fields[3] )
                self.block_info.append( ( offset, compressed_size, size ) )
        self.nblocks = len( self.block_info )
        
    def close( self ):
        self.file.close()
        
    def load_block( self, index ):
        if self.cache is not None and index in self.cache:
            return self.cache[index]
        else:      
            offset, csize, size = self.block_info[ index ]
            # Get the block of compressed data
            self.file.seek( offset )
            data = self.file.read( csize )
            # Need to prepend a header for python-lzo module (silly)
            data = b''.join( ( b'\xf0', struct.pack( "!I", size ), data ) )
            value = lzo.decompress( data )
            if self.cache is not None:
                self.cache[index] = value
            return value
        
    def fix_dirty( self ):
        chunk, offset = self.get_block_and_offset( self.file_pos )
        if self.current_block_index != chunk:
            self.current_block = BytesIO( self.load_block( chunk ) )
            self.current_block.read( offset )
            self.current_block_index = chunk
        else:
            self.current_block.seek( offset )
        self.dirty = False
        
    def get_block_and_offset( self, index ):
        return int( index // self.block_size ), int( index % self.block_size )

    def seek( self, offset, whence=0 ):
        """
        Move the file pointer to a particular offset.
        """
        # Determine absolute target position
        if whence == 0:
            target_pos = offset
        elif whence == 1:
            target_pos = self.file_pos + offset
        elif whence == 2:
            raise Exception( "seek from end not supported" )
            ## target_pos = self.size - offset
        else:
            raise Exception( "Invalid `whence` argument: %r", whence )
        # Check if this is a noop
        if target_pos == self.file_pos:
            return    
        # Verify it is valid
        ## assert 0 <= target_pos < self.size, "Attempt to seek outside file"
        # Move the position
        self.file_pos = target_pos
        # Mark as dirty, the next time a read is done we need to actually
        # move the position in the bzip2 file
        self.dirty = True
        
    def tell( self ):
        return self.file_pos
        
    def readline( self ):
        if self.dirty:
            self.fix_dirty()
        if self.at_eof:
            return b""
        rval = []
        while 1:
            line = self.current_block.readline()
            self.file_pos += len( line )
            rval.append( line )
            if len( line ) > 0 and line[-1] == b'\n':
                break
            elif self.current_block_index == self.nblocks - 1:
                self.at_eof = True
                break
            else:
                self.current_block_index += 1
                self.current_block = BytesIO( self.load_block( self.current_block_index ) )
        return b"".join( rval )
            
    def __next__( self ):
        line = self.readline()
        if line == b"":
            raise StopIteration
            
    def __iter__( self ):
        return self

# --- Factor out ---        
        
MAGIC=b"\x89\x4c\x5a\x4f\x00\x0d\x0a\x1a\x0a"

F_ADLER32_D     = 0x00000001
F_ADLER32_C     = 0x00000002
F_H_EXTRA_FIELD = 0x00000040
F_H_GMTDIFF     = 0x00000080
F_CRC32_D       = 0x00000100
F_CRC32_C       = 0x00000200
F_MULTIPART     = 0x00000400
F_H_FILTER      = 0x00000800
F_H_CRC32       = 0x00001000

assert struct.calcsize( "!H" ) == 2
assert struct.calcsize( "!I" ) == 4

class UnpackWrapper( object ):
    def __init__( self, file ):
        self.file = file
    def read( self, amt ):
        return self.file.read( amt )
    def get( self, fmt ):
        t = struct.unpack( fmt, self.file.read( struct.calcsize( fmt ) ) )
        return t[0]
