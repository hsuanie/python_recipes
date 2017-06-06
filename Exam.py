# Programming practices in Python course in IBI HU Berlin
#!/usr/bin/python
import re
line = "I have a love and hate relationship with Python programming."
matchObj = re.match( r'(.*) really .*? a (.*) - (.*) .*? with (.*)', line)
if matchObj:
   print "I", matchObj.group(2),matchObj.group(4)
else:
   print "No match!!"