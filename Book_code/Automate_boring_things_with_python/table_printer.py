# Prints well organised tables

# Old school version -----
# you can think x and y as coordinates
# def printTable(table):
#     # create a list with the length of the longest string
#     colWidth = [0]*len(table)
#     for y in range(len(table)):
#         for x in table[y]:
#             if colWidth[y]<len(x):
#                 colWidth[y]=len(x)
    
#     # rotate and print the list of lists
#     for x in range(len(table[0])):
#         for y in range(len(table)):
#             print(table[y][x].rjust(colWidth[y]),end=" ")
#         print()

# New & improved version----- 
def print_table(table):
    
    # create the maxwidth list
    col_width = [max(len(item) for item in record) for record in table]

    # join all the first item in each list of list
    for i in range(len(table[0])):
        print(" ".join(record[i].rjust(col_width[j]) for j,record in enumerate(table)))

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


print_table(tableData)

