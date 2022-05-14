'''
Load a text file as a list

Arguments:
- Text file name

Exceptions:
- IOError if filename not found

Returns:
- A list of all words in the text file in lower case

Requires:
- import sys
'''
import sys

def load(file):
    '''Opens a text file and returns a list of lowercase strings'''
    try:
        with open(file) as f:
            loaded_txt = f.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f'{e}\nError opening {file}. Terminating Program.', file=sys.stderr)
        sys.exit(1)