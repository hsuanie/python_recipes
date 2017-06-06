# Programming practices in Python course in IBI HU Berlin
from sys import argv

script, filename = argv

txt = open (filename)

print "This is your %r:"% filename
print txt.read()

print "Type the filename again:"

file_again = raw_input('> ')
txt_again = open (file_again)
print txt_again.read()