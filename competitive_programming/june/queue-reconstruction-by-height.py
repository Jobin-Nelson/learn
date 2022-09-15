'''
Created Date: 29-06-2022
Qn: You are given an array of people, people, which are the attributes of some 
    people in a queue (not necessarily in order). Each people[i] = [hi, ki] 
    represents the ith person of height hi with exactly ki other people in front 
    who have a height greater than or equal to hi.
    Reconstruct and return the queue that is represented by the input array people. 
    The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] 
    is the attributes of the jth person in the queue (queue[0] is the person at 
    the front of the queue).
Link: https://leetcode.com/problems/queue-reconstruction-by-height/
Notes:
    - sort the list
    - track the people ahead and insert the values to a new list
'''
def reconstructQueue(people: list[list[int]]) -> list[list[int]]:
    N = len(people)
    res = [None] * N
    people.sort()

    for height, q in people:
        i, j = 0, -1
        while i < N:
            if not res[i] or res[i][0] == height:
                j += 1
            if j == q:
                break
            i += 1
        res[i] = [height, q]
    return res

if __name__ == '__main__':
    p1 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    p2 = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(reconstructQueue(p1))
    print(reconstructQueue(p2))
