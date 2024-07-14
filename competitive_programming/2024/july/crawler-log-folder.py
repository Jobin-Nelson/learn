"""
Created Date: 2024-07-10
Qn: The Leetcode file system keeps a log each time some user performs a change
    folder operation.

    The operations are described below:

    - "../" : Move to the parent folder of the current folder. (If you are
      already in the main folder, remain in the same folder). 
    - "./" : Remain in the same folder. 
    - "x/" : Move to the child folder named x (This folder is guaranteed to
      always exist). You are given a list of strings logs where logs[i] is the
      operation performed by the user at the ith step.

    The file system starts in the main folder, then the operations in logs are
    performed.

    Return the minimum number of operations needed to go back to the main
    folder after the change folder operations.
Link: https://leetcode.com/problems/crawler-log-folder/
Notes:
    - use stack or simulation
"""
def minOperations(logs: list[str]) -> int:
    res = 0
    for o in logs:
        if o == '../':
            if res > 0:
                res -= 1
        elif o != './':
            res += 1
    return res

if __name__ == '__main__':
    l1 =    ["d1/","d2/","../","d21/","./"]
    l2 = ["d1/","d2/","./","d3/","../","d31/"]
    l3 = ["d1/","../","../","../"]
    l4 = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]

    print(minOperations(l1))
    print(minOperations(l2))
    print(minOperations(l3))
    print(minOperations(l4))
