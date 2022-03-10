# Write a program to merge two lists and return it as a sorted list with no repeating values.
# - Input: list1 = [2,3,4,4], list2 = [1,3,4,5,3]
# - Output: [1,2,3,4,5]

list1 = [2,3,4,4] 
list2 = [1,3,4,5,3]
list1.extend(list2)
print(list1)
new_list = list(set(list1))
print(new_list)

