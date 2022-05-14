import sys
from collections import Counter
import load_dictionary

dict_file = load_dictionary.load('words.txt')
dict_file.extend(['a', 'i'])
dict_file = sorted(dict_file)

ini_name = input('Enter a name: ')

def find_anagrams(name, word_list):
    '''
    Read name & dictionary file & display all anagrams in name
    '''
    name_letter_map = Counter(name)
    anagrams = []

    for word in word_list:
        word_letter_map = Counter(word.lower())
        test = ''

        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    
    print(*anagrams, sep='\n')
    print(f'\nRemaining letters = {name}')
    print(f'Number of remaining letters = {len(name)}')
    print(f'Number of remaining (real word) anagrams = {len(anagrams)}')

def process_choice(name):
    '''
    Check user choice for validity, returns choice & left over letters
    '''
    while True:
        choice = input('\nMake a choice else Enter to start over or # to exit:')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("Won't work! Make another choice!", file=sys.stderr)
    name = ''.join(left_over_list)
    return choice, name

def main():
    '''
    Help user build anagram phrase from their names
    '''
    name = ''.join(ini_name.lower().split())
    name = name.replace('-','')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f'Length of anagram phrase = {len(temp_phrase)}')
            find_anagrams(name, dict_file)
            print('Current anagrams phrase = ', phrase)

            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print('\n*****FINISHED!!!*****\n')
            print('Anagram of name =', end=' ')
            print(phrase, file=sys.stderr)
            try_again = input('\nTry again? (Press Enter else n to quit)')
            if try_again.lower() == 'n':
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()
