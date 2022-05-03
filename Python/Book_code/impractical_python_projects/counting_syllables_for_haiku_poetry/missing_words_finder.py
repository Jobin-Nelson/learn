import json
import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict() # Carnegie Mellon Unviersity Pronouncing Dictionary

def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input('\nManually build an exceptions dictionary (y/n)? \n')
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict)

def load_haiku(filename):
    '''Open and return training corpus of haiku as a set'''
    with open(filename) as f:
        haiku = set(f.read().replace('-', ' ').split())
        return haiku

def cmudict_missing(word_set):
    '''Find and return words in word set missing from cmudict'''
    exceptions = set()
    for word in word_set():
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print('\nExceptions: ')
    print(*exceptions, sep='\n')
    print('\nNumber of unique words in haiku corpus', len(word_set))
    print('\nNumber of words in corpus not in cmudict =', len(exceptions))
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print(f'cmudict membership = {membership:.1f}%')
    return exceptions

def make_exceptions_dict(exceptions_set):
    '''Return dictionary of words & syllable counts from a set of words'''
    missing_words = {}
    print('Input # syllables in word. Mistakes can be corrected at the end')
    for word in exceptions_set:
        while True:
            num_sylls = input(f'Enter number syllables in {word}: ')
            if num_sylls.isdigit():
                break
            else:
                print('Not a valid answer!', file=sys.stderr)
        missing_words[word] = int(num_sylls)
    print()
    pprint.pprint(missing_words, width=1)

    print('\nMake Changes to Dictionary Before Saving?')
    print('''
    0 - Save & Exit
    1 - Add a Word or Change a Syllable Count
    2 - Remove a Word
    ''')

    while True:
        choice = input('\nEnter Choice: ')
        if choice == '0':
            break
        if choice == '1':
            word = input('\nWord to add or change: ')
            missing_words[word] = int(input('Enter number syllables in', word))
        elif choice == '2':
            missing_words.pop(word, None)
    print('\nNew words or syllables changes:')
    pprint.pprint(missing_words, width=1)
    return missing_words

def save_exceptions(missing_words):
    '''Save exceptions dictionary as a json file'''
    json_string = json.dumps(missing_words)
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print('\nFile saved as missing_words.json')

if __name__ == '__main__':
    main()
    