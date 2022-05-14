''' 
Decrypt a path through Union Route Cipher

Designed for whole-word transposition ciphers with variable rows & columns
Assumes encryption began at either top or bottom of a column
Key indicates the order to read columns and the direction to traverse
Negative column numbers mean start at bottom and read up
Positive column numbers mean start at top and read down

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.
	1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string
Prints translated plaintext
'''
import sys

#====================================================================
# USER INPUT:

# the string to be decrypted (type of paste between triple quotes)
ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS
                OF AT WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE
                TRIBUNE PLEASE ARE THEM CAN UP"""

# number of columns in transposition matrix:
COLS = 4

# number of rows in transposition matrix:
ROWS = 6

# key with spaces between numbers; negative to read UP column (ex= -1 2 -3 4):
key = """-1 2 -3 4"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#====================================================================

def main():
    ''' Run program and print decrypted plaintext '''
    print('\nCiphertext =', ciphertext)
    print(f'Trying {COLS} columns')
    print(f'Trying {ROWS} columns')
    print(f'Trying {key=}')

    # split elements into words, not letters
    cipherlist = ciphertext.split()
    validate_col_row(cipherlist)
    key_int = key_to_int(key)
    translation_matrix = build_matrix(key_int, cipherlist)
    plaintext = decrypt(translation_matrix)

    print(f'{plaintext=}')

def validate_col_row(cipherlist):
    ''' Check that input columns and rows are valid vs message length '''
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
    
    print('\nLength of cipher =', len_cipher)
    print('Acceptable column/rows values include:', factors)

    if ROWS * COLS != len_cipher:
        print('\nError - Input rows & columns not factor of length of cipher')
        print('Terminating program')
        sys.exit(1)

def key_to_int(key):
    '''Turn key into list of integers & check validity'''
    key_int = [int(i) for i in key.split()]
    if len(key_int) != COLS or min(key_int) < -COLS or max(key_int) > COLS or 0 in key_int:
        print('\nError - Problem with key. \nTerminating')
        sys.exit(1)
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    '''Turn every item in the list to a new item in a list of lists'''
    translation_matrix = [None] * COLS
    start = 0
    stop = ROWS

    for k in key_int:
        if k < 0: # read from bottom to top of column
            col_item = cipherlist[start:stop]
        elif k > 0: # read from top to bottom of column
            col_item = list(reversed(cipherlist[start:stop]))
        translation_matrix[abs(k)-1] = col_item
        start += ROWS
        stop += ROWS
    return translation_matrix

def decrypt(translation_matrix):
    '''Loop through nested lists popping off last item to a string'''
    plaintext = ''
    for i in range(ROWS):
        for matrix_col in translation_matrix:
            plaintext += str(matrix_col.pop()) + ' '
    return plaintext

if __name__ == '__main__':
    main()