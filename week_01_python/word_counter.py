import pprint
import string

text = open("onefish_twofish.txt", "r")
# print(text.readline())

# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
words = {}
'name' in words.keys()

for line in text:
    line_list = line.split(" ")
    for word in line_list:
        word = word.lower().strip()
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word in words.keys():
            words[word] = words[word]+1
        else:
            words[word] = 1

pprint.pprint(words)

text.close()