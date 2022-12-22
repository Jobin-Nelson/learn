'''
Created Date: 2022-12-20
Qn: There are n rooms labeled from 0 to n - 1 and all the rooms are locked
    except for room 0. Your goal is to visit all the rooms. However, you cannot
    enter a locked room without having its key.

    When you visit a room, you may find a set of distinct keys in it. Each key
    has a number on it, denoting which room it unlocks, and you can take all of
    them with you to unlock the other rooms.

    Given an array rooms where rooms[i] is the set of keys that you can obtain
    if you visited room i, return true if you can visit all the rooms, or false
    otherwise.
Link: https://leetcode.com/problems/keys-and-rooms/
Notes:
    - use set to remove keys as we visit, and stack to add keys as we visit
'''
def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    pool, stack = set(range(len(rooms))), [0]

    while stack:
        pool.discard(stack[-1])
        for nei in rooms[stack.pop()]:
            if nei in pool: stack.append(nei)
    return not pool

if __name__ == '__main__':
    r1 = [[1],[2],[3],[]]
    r2 = [[1,3],[3,0,1],[2],[0]]
    
    print(canVisitAllRooms(r1))
    print(canVisitAllRooms(r2))
