# Data structure

A data structure is a particular way of organizing data in a computer so that
it can be used effectively. The idea is to reduce time and space complexities
of different tasks

- **Array**: The array is a data structure used to store homogeneous elements
  at contiguous locations. The size of an array must be provided before storing
  data.

- **Linked List**: A linked list is a linear data structure (like arrays) where
  each element is a separate object. Each element (that is node) of a list is
  comprised of two items – the data and a reference to the next node.

- **Stack**: A stack or LIFO (last in, first out) is an abstract data type that
  serves as a collection of elements, with two principal operations: push,
  which adds an element to the collection, and pop, which removes the last
  element that was added. In stack both the operations of push and pop take
  place at the same end that is top of the stack. It can be implemented by
  using both array and linked list.

- **Queue**: A queue or FIFO (first in, first out) is an abstract data type
  that serves as a collection of elements, with two principal operations:
  enqueue, the process of adding an element to the collection. (The element is
  added from the rear side) and dequeue the process of removing the first
  element that was added. (The element is removed from the front side). It can
  be implemented by using both array and linked list.

- **Binary Tree**: Unlike Arrays, Linked Lists, Stack, and queues, which are
  linear data structures, trees are hierarchical data structures. 
    - A binary tree is a tree data structure in which each node has at most two
      children, which are referred to as the left child and the right child. It
      is implemented mainly using Links. 
    - Binary Tree Representation: A tree is represented by a pointer to the
      topmost node in the tree. If the tree is empty, then the value of the
      root is NULL. A Binary Tree node contains the following parts. 
        1. Data 
        2. Pointer to left child 
        3. Pointer to the right child 

- **Binary Search Tree**: In Binary Search Tree is a Binary Tree with the
  following additional properties: 
    1. The left subtree of a node contains only nodes with keys less than the
    node’s key. 
    2. The right subtree of a node contains only nodes with keys greater than
    the node’s key. 
    3. The left and right subtree each must also be a binary search tree.

- **Heap**: A Binary Heap is a Binary Tree with the following properties. 1)
  It’s a complete tree (All levels are completely filled except possibly the
  last level and the last level has all keys as left as possible). This
  property of Binary Heap makes them suitable to be stored in an array. 2) A
  Binary Heap is either Min Heap or Max Heap. In a Min Binary Heap, the key at
  the root must be minimum among all keys present in Binary Heap. The same
  property must be recursively true for all nodes in Binary Tree. Max Binary
  Heap is similar to Min Heap. It is mainly implemented using an array. 

- **Hash Table**: An array that stores pointers to records corresponding to a
  given phone number. An entry in a hash table is NIL if no existing phone
  number has a hash function value equal to the index for the entry. 

- **Graph**: Graph is a data structure that consists of following two
  components:
    1. A finite set of vertices also called as nodes.
    2. A finite set of ordered pair of the form (u, v) called as edge. The pair
    is ordered because (u, v) is not same as (v, u) in case of directed
    graph(di-graph). The pair of form (u, v) indicates that there is an edge
    from vertex u to vertex v. The edges may contain weight/value/cost.
        - V -> Number of Vertices.
        - E -> Number of Edges.
