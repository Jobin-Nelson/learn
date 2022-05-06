import sys
import count_syllables

with open('train.txt') as f:
    words = set(f.read().split())

missing = []

for word in words:
    try:
        num_syllables = count_syllables.count_syllables(word)
        #print(word, num_syllables) # uncomment to see word counts
    except KeyError:
        missing.append(word)

print('Missing words:', missing, file=sys.stderr)