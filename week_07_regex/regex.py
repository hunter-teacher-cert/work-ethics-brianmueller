# Grab the regex.py code from the class site. Modify it so that it reads
# a text file and uses regexes to find as many names in the text file as
# possible. For example "John Smith" would be a name as would "Mrs. Cho."
# Remember that you will likely have to use multiple regular expressions
# to handle different cases just like we did in class to identify dates.
# Create or edit your text file so that it has data to read in and test
# itself on.
# When run, your program should print out all the names it finds. Don't
# worry about formatting, you can just print the results of your calls
# to re.findall() or any other calls you make.

import re


def find_name(line):

    pattern = r"([M]?(r|s|rs|iss)?\.?\ ?[A-Z][a-z]*\ [A-Z][a-z]*)"
    result = re.findall(pattern,line)

    return result

f = open("namefile.dat")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
