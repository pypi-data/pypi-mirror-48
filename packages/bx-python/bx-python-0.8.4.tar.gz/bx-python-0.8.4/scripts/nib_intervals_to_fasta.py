#!/usr/bin/env python

"""
Read a set of ranges and a nib file, print portions of nib overlapping
those ranges to stdout

usage: %prog range_file nib_file
"""
from __future__ import print_function

import string
import sys

import bx.seq.nib
from bx.cookbook import doc_optparse


def __main__():

    options, args = doc_optparse.parse( __doc__ )

    try:
        range_file = file( args[0] )
        nib_file = file( args[1] )
    except:
        doc_optparse.exit()

    nib = bx.seq.nib.NibFile( nib_file )

    for line in range_file: 
        fields = line.split()
        start, end = int( fields[0] ), int( fields[1] ) 
        print(">", start, end)
        print_wrapped( nib.get( start, end - start ) )

def print_wrapped( s ):
    l = len( s )        
    c = 0
    while c < l:
        b = min( c + 50, l )
        print(s[c:b])
        c = b

if __name__ == "__main__":
    __main__()
