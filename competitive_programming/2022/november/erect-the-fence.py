'''
Created Date: 2022-11-19
Qn: You are given an array trees where trees[i] = [xi, yi] represents the
    location of a tree in the garden.

    You are asked to fence the entire garden using the minimum length of rope
    as it is expensive. The garden is well fenced only if all the trees are
    enclosed.

    Return the coordinates of trees that are exactly located on the fence
perimeter.
Link: https://leetcode.com/problems/erect-the-fence/
Notes:
    - use cross product to find the slope
    - first construct going from left to right (lower half of hull) then 
    - then construct going from right to left (upper half of hull)
'''
def outerTrees(trees: list[list[int]]) -> list[list[int]]:
    def crossProduct(p1, p2, p3):
        # V1 = (a, b), V2 = (c, d)
        # V! * V2 = a * d - b * c
        a = p2[0] - p1[0]
        b = p2[1] - p1[1]
        c = p3[0] - p1[0]
        d = p3[1] - p1[1]
        return a * d - b * c

    def constructHalfHull(points):
        stack = []
        for p in points:
            # if the last two points in the stack is not counter-clockwise, pop it
            while len(stack) >= 2 and crossProduct(stack[-2], stack[-1], p) > 0:
                stack.pop()
            stack.append(tuple(p))
        return stack

    trees.sort()
    leftToRight = constructHalfHull(trees)
    rightToLeft = constructHalfHull(trees[::-1])
    return list(set(leftToRight + rightToLeft))

if __name__ == '__main__':
    p1 = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    p2 = [[1,2],[2,2],[4,2]]

    print(outerTrees(p1))
    print(outerTrees(p2))
