'''
Created Date: 2022-09-19
Qn: Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

    A group of duplicate files consists of at least two files that have the same
    content.

    A single directory info string in the input list has the following format:

        - "root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ...

    fn.txt(fn_content)" It means there are n files (f1.txt, f2.txt ... fn.txt) with
    content (f1_content, f2_content ... fn_content) respectively in the directory
    "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the
    directory is just the root directory.

    The output is a list of groups of duplicate file paths. For each group, it
    contains all the file paths of the files that have the same content. A file
    path is a string that has the following format:

        - "directory_path/file_name.txt"
Link: https://leetcode.com/problems/find-duplicate-file-in-system/
Notes:
    - hashmap with key as content and values as files
'''
from collections import defaultdict

def findDuplicate(paths: list[str]) -> list[list[str]]:
    c = defaultdict(list)

    for path in paths:
        path = path.split()
        folder = path[0]
        for s in path[1:]:
            name, content = s.split('.txt')
            c[content].append((folder, name))

    output = []

    for _, v in c.items():
        if len(v) > 1:
            tmp = []

            for path, name in v:
                tmp.append(path + '/' + name + '.txt')
            output.append(tmp)
    return output

if __name__ == '__main__':
    p1 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    p2 = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]

    print(findDuplicate(p1))
    print(findDuplicate(p2))
