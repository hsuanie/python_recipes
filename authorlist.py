import re


searchFor = "t.*?"
searchFor = "<author>*?"

s = re.findall(r'%s \w*' % searchFor, line, flags=re.IGNORECASE)
