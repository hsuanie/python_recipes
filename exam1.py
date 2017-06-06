# Programming practices in Python course in IBI HU Berlin
import re
line = "I hope this is the easiest exam ever at Humboldt University in Berlin" 
matchObj = re.match( r'(.*) the .*? or (.*) ever (.*)', line)

if matchObj:
	print "matchObj.group(2) : ", matchObj.group(2) 

else:
	print "No match!!"