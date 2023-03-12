'''
Created Date: 2023-03-05
Qn: Given an array of integers arr, you are initially positioned at the first
    index of the array.

    In one step you can jump from index i to index:

        - i + 1 where: i + 1 < arr.length.
        - i - 1 where: i - 1 >= 0.
        - j where: arr[i] == arr[j] and i != j.

    Return the minimum number of steps to reach the last index of the array.

    Notice that you can not jump outside of the array at any time.
Link: https://leetcode.com/problems/jump-game-iv/
Notes:
    - use bfs
    - use defaultdict to group indices based on value
'''
from collections import defaultdict, deque

def minJumps(arr: list[int]) -> int:
    N = len(arr)

    indices = defaultdict(list)
    for i in range(N):
        indices[arr[i]].append(i)

    storeIndex = deque([0])
    visited = [False] * N
    visited[0] = True
    step = 0

    while storeIndex:
        for _ in range(len(storeIndex)):
            curIndex = storeIndex.popleft()
            if curIndex == N-1: return step

            jumpNextIndices = indices[arr[curIndex]]
            jumpNextIndices.append(curIndex-1)
            jumpNextIndices.append(curIndex+1)

            for jumpNextIndex in jumpNextIndices:
                if 0 <= jumpNextIndex < N and not visited[jumpNextIndex]:
                    storeIndex.append(jumpNextIndex)
                    visited[jumpNextIndex] = True
            jumpNextIndices.clear()
        step += 1
    return -1

if __name__ == '__main__':
    a1 = [100,-23,-23,404,100,23,23,23,3,404]
    a2 = [7]
    a3 = [7,6,9,6,9,6,9,7]

    print(minJumps(a1))
    print(minJumps(a2))
    print(minJumps(a3))
