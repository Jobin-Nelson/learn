# Hashmap
- Need for hashmap
	- array are effeceint at retriving values using index, but they fall apart when new elements are being added into the array which necessitates copying over the entire array to make room for new elements
	- linked lists solves the problem of adding new elements to arrays but introduces a new problem, if we want to search for an element in linked lists we have to traverse the whole linked lists comparing the element at each node

- Hashmap solves the problem of looking up an element and also doesn't have the issue with adding new elements
- It is done by key value pairs, where the key is given to a hashing function which outputs an integer which is index value where the element would be stored this makes the run time complexity of searching, adding and deleting operations a O(1)
- However there are issues with hashmaps such as collision which happens when two keys gives the same index this could be solved by linear probing or seperate chaining
	- linear probing is done by assigning the new element to next free index in the hashtable
	- seperate chaining is done by essentially pointing to a linked list, it is preferred over linear probing
