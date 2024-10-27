"""
Created Date: 2024-10-25
Qn: Given a list of folders folder, return the folders after
    removing all sub-folders in those folders. You may
    return the answer in any order.

    If a folder[i] is located within another folder[j], it
    is called a sub-folder of it. A sub-folder of folder[j]
    must start with folder[j], followed by a "/". For
    example, "/a/b" is a sub-folder of "/a", but "/b" is not
    a sub-folder of "/a/b/c".

    The format of a path is one or more concatenated strings
    of the form: '/' followed by one or more lowercase
    English letters.

    For example, "/leetcode" and "/leetcode/problems" are
    valid paths while an empty string and "/" are not.
Link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
Notes:
    - use prefix tree data structure
"""


class Trie:
    def __init__(self):
        self.subfolders = {}
        self.is_path = False

    def add(self, path):
        cur = self
        for f in path.split('/'):
            if f not in cur.subfolders:
                cur.subfolders[f] = Trie()
            cur = cur.subfolders[f]
        cur.is_path = True

    def is_subfolder(self, path) -> bool:
        cur = self
        for f in path.split('/'):
            if cur.is_path:
                return True
            cur = cur.subfolders[f]
        return False


def removeSubFolders(folder: list[str]) -> list[str]:
    trie = Trie()
    for f in folder:
        trie.add(f)
    return [f for f in folder if not trie.is_subfolder(f)]


if __name__ == '__main__':
    f1 = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    f2 = ["/a", "/a/b/c", "/a/b/d"]
    f3 = ["/a/b/c", "/a/b/ca", "/a/b/d"]
    print(removeSubFolders(f1))
    print(removeSubFolders(f2))
    print(removeSubFolders(f3))
