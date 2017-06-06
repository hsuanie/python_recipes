# Programming practices in Python course in IBI HU Berlin
#! /usr/bin/python

# IMPORT STANDARD FUNCTIONS
import string, os, fnmatch, sys, re, urllib2, time

# DEFINE VARIABLES
line_tot = h_num = 0

# INDICATE PROGRAM START ON CONSOLE

print '\nSTART TIME:', time.asctime( time.localtime(time.time()) ), '\n'

startURL = sys.argv[1]
print startURL
search = '(.href=")(//.*?)(")' 

myurl = urllib2.urlopen(startURL)
source = myurl.readlines()

# WORK THROUGH LINES IN THE SOURCE
for line in source:
  m = re.findall(search,line)
#m = re.match (r'(.+ digital.*).(librar.+)',line)
  if m:
    l = len(m)
    for n in range (0,l):
      url= m[n]
      fullurl = 'http:'+ url[1]
      print fullurl
 #### END