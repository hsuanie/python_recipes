# Programming practices in Python course in IBI HU Berlin
#! /usr/bin/python

# IMPORT STANDARD FUNCTIONS
import string, os, fnmatch, sys, re

#INCLUDE COMMENTS TO DOCUMENT WHAT YOU ARE DOING
#EXAMPLE OF READING A FILE
file = sys.argv[1]

f = open (file, 'r')

for line in f:
    print line

f.close()

