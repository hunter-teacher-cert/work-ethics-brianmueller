import random

words1 = ['software','engineering','program','computer','science','algorithm','digital','github','website','high','school','of','telecommunication','arts','and','technology']

# print words1

def print_all(words):
  for word in words:
    print(word.upper())

print_all(words1)
print('')

def scramble(word):
  word_list = list(word)
  random.shuffle(word_list)
  return ''.join(word_list)

# print scramble('software')

def scramble_all(words):
  scrambled_words = []
  for word in words:
    scrambled_words.append(scramble(word))
  return scrambled_words

words1_scrambled = scramble_all(words1)
print_all(words1_scrambled)