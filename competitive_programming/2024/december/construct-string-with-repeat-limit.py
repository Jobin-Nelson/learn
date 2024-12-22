"""
Created Date: 2024-12-17
Qn: You are given a string s and an integer repeatLimit. Construct a new string
    repeatLimitedString using the characters of s such that no letter appears
    more than repeatLimit times in a row. You do not have to use all characters
    from s.

    Return the lexicographically largest repeatLimitedString possible.

    A string a is lexicographically larger than a string b if in the first
    position where a and b differ, string a has a letter that appears later in
    the alphabet than the corresponding letter in b. If the first min(a.length,
    b.length) characters do not differ, then the longer string is the
    lexicographically larger one.
Link: https://leetcode.com/problems/construct-string-with-repeat-limit/
Notes:
    - use heap
"""

import unittest
from collections import Counter
import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        heap = [(-ord(c), cnt) for c, cnt, in count.items()]
        heapq.heapify(heap)
        res = []

        while heap:
            ch, cnt = heapq.heappop(heap)
            ch = chr(-ch)
            cur_cnt = min(cnt, repeatLimit)
            res.append(ch * cur_cnt)

            if cnt - cur_cnt > 0 and heap:
                nxt_ch, nxt_cnt = heapq.heappop(heap)
                nxt_ch = chr(-nxt_ch)
                res.append(nxt_ch)
                if nxt_cnt > 1:
                    heapq.heappush(heap, (-ord(nxt_ch), nxt_cnt - 1))
                heapq.heappush(heap, (-ord(ch), cnt - cur_cnt))
        return ''.join(res)



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_repeatLimitedString1(self):
        s, r = "cczazcc", 3
        expected = "zzcccac"
        self.assertEqual(expected, self.sol.repeatLimitedString(s, r))

    def test_repeatLimitedString2(self):
        s, r = "aababab", 2
        expected = "bbabaa"
        self.assertEqual(expected, self.sol.repeatLimitedString(s, r))


if __name__ == '__main__':
    unittest.main()
