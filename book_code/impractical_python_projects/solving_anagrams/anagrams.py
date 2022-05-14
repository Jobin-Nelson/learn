import load_dictionary

word_list = load_dictionary.load('words.txt')

anagram = input('Give me a word to search for its anagrams: ')
sorted_anagram = sorted(anagram.lower())
res = []

for word in word_list:
    if word != anagram and sorted(word.lower()) == sorted_anagram:
        res.append(word)

if len(res) > 0:
    print(f'Anagrams of {anagram} are: ')
    print(*res, sep='\n')
else:
    print('You need a larger dictionary')