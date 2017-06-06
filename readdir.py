# Programming practices in Python course in IBI HU Berlin
# IMPORT STANDARD FUNCTIONS
import string, os, fnmatch, sys, re

#SET VARIABLES
fileno = 0
ffile = [] #CREATE LIST

#EXAMINE THE DIRECTORY AND IF THE TITEL IS ICONF*.TXT, THEN ADD TO THE LIST

for file in os.listdir('/Users/hsuan/Documents/iConference'):
  if fnmatch.fnmatch (file, 'iConf*.txt'):
    ffile.append (file)
    fileno +=1

#PRINT ALL THE FILES IN THE LIST

for n in range (0,fileno):
    print 'from for loop', ffile[n]