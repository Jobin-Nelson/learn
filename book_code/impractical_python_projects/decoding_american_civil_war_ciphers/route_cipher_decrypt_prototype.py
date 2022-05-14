ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# spilt elements into words, not letters
cipherlist = ciphertext.split()

# intializes variables
cols = 4
rows = 5
key = '-1 2 -3 4' # negative number means read up
translation_matrix = [None] * cols
plaintext = ''
start = 0
stop = rows

# turn key into list of integers
key_int = list(map(int, key.split()))

# turn columns into items in list of lists
for k in key_int:
    if k < 0:
        col_items = cipherlist[start:stop]
    elif k > 0:
        col_items = list(reversed(cipherlist[start:stop]))
    translation_matrix[abs(k)-1] = col_items
    start += rows
    stop += rows

print('ciphertext = ', ciphertext)
print('translation_matrix : ', *translation_matrix, sep='\n')
print('key length =', len(key_int))

# loop through nested lists popping off last item to new list
for i in range(rows):
    for col_items in translation_matrix:
        word = str(col_items.pop())
        plaintext += word + ' '

print(f'{plaintext=}')

