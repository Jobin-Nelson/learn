# Dynamic Programming

- Notice any overlapping subproblems
- Decide what is the trivially smallest input
- Think recursively to use *memoization*
- Think iteratively to use *tabulation*
- Draw a strategy first!!!

## Memoization Recipe

1. Make it work
	- visualize the problem as a tree
	- implement the tree using recursion
	- test it

2. Make it efficient
	- add a memo object
	- add a base case to return stored memo values
	- store return values into the memo

## Tabulation recipe

- Visualize the problem as a table
- Size the table based on the inputs
- Initialize the table with default values
- Seed the trivial answer into the table
- Iterate through the table
- Fill further positions based on the current position
