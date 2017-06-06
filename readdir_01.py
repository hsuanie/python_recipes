# Programming practices in Python course in IBI HU Berlin
import string, os, fnmatch, sys, re
# IMPORT STANDARD FUNCTIONS import string, os, fnmatch, sys, re
#SET VARIABLES

fileno = 0
ffile = [] #CREATE LIST

#GET VARIABLES FORM COMMAND LINE 
inputLine = sys.argv[1]
#inputLine = iConf*.txt
#EXAMINE THE DIRECTORY 
currentDirectory = os.getcwd()
for file in os.listdir(currentDirectory):
	if fnmatch.fnmatch (file, inputLine): ffile.append (file)
	fileno +=1

#PRINT ALL THE FILES IN THE LIST 
for n in range (0,fileno):
	print "Files in directory", ffile[n]