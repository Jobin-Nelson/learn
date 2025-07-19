"""
Created Date: 2025-07-19
Qn: Given a list of folders folder, return the folders after removing all
    sub-folders in those folders. You may return the answer in any order.

    If a folder[i] is located within another folder[j], it is called a
    sub-folder of it. A sub-folder of folder[j] must start with folder[j],
    followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is
    not a sub-folder of "/a/b/c".

    The format of a path is one or more concatenated strings of the form: '/'
    followed by one or more lowercase English letters.

    - For example, "/leetcode" and "/leetcode/problems" are valid paths while
      an empty string and "/" are not
Link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
Notes:
    - sort and check last folder
"""

import unittest


class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        res = [folder[0]]
        for f in folder[1:]:
            last_folder = res[-1] + '/'
            if not f.startswith(last_folder):
                res.append(f)
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_removeSubfolders1(self):
        f = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
        expected = ["/a", "/c/d", "/c/f"]
        self.assertEqual(expected, self.sol.removeSubfolders(f))

    def test_removeSubfolders2(self):
        f = ["/a", "/a/b/c", "/a/b/d"]
        expected = ["/a"]
        self.assertEqual(expected, self.sol.removeSubfolders(f))

    def test_removeSubfolders3(self):
        f = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        expected = ["/a/b/c", "/a/b/ca", "/a/b/d"]
        self.assertEqual(expected, self.sol.removeSubfolders(f))


if __name__ == '__main__':
    unittest.main()
