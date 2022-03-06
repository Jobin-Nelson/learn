# print well organised tables
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    # get maximum length of each record
    max_len = [max(len(item) for item in record) for record in table]
    
    for i in range(len(table[0])):
        print(' '.join(record[i].rjust(max_len[j]) for j,record in enumerate(table)))

print_table(tableData)