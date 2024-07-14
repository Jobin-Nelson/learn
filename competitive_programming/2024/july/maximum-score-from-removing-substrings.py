"""
Created Date: 2024-07-12
Qn: You are given a string s and two integers x and y. You can perform two
    types of operations any number of times.

        - Remove substring "ab" and gain x points. 
            - For example, when removing "ab" from "cabxbae" it becomes
              "cxbae". 
        - Remove substring "ba" and gain y points.
            - For example, when removing "ba" from "cabxbae" it becomes
              "cabxe". 

      Return the maximum points you can gain after applying the above
      operations on s.
Link: https://leetcode.com/problems/maximum-score-from-removing-substrings/
Notes:
    - use stack
"""
def maximumGain(s: str, x: int, y: int) -> int:
    def remove_pairs(pair: str, score: int) -> int:
        nonlocal s
        res = 0
        stack = []

        for c in s:
            if c == pair[1] and stack and stack[-1] == pair[0]:
                stack.pop()
                res += score
            else:
                stack.append(c)
        s = ''.join(stack)
        return res

    res = 0
    pair = "ab" if x > y else "ba"
    res += remove_pairs(pair, max(x,y))
    res += remove_pairs(pair[::-1], min(x,y))
    return res

if __name__ == '__main__':
    s1, x1, y1 = "cdbcbbaaabab", 4, 5
    s2, x2, y2 = "aabbaaxybbaabb", 5, 4

    print(maximumGain(s1, x1, y1))
    print(maximumGain(s2, x2, y2))
