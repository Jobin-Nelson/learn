'''
Created Date: 2023-04-12
Qn: Given a string path, which is an absolute path (starting with a slash '/')
    to a file or directory in a Unix-style file system, convert it to the
    simplified canonical path.

    In a Unix-style file system, a period '.' refers to the current directory,
    a double period '..' refers to the directory up a level, and any multiple
    consecutive slashes (i.e. '//') are treated as a single slash '/'. For this
    problem, any other format of periods such as '...' are treated as
    file/directory names.

    The canonical path should have the following format:

        - The path starts with a single slash '/'. 
        - Any two directories are separated by a single slash '/'. 
        - The path does not end with a trailing '/'. 
        - The path only contains the directories on the path from the root
          directory to the target file or directory (i.e., no period '.' or
          double period '..')

    Return the simplified canonical path.
Link: https://leetcode.com/problems/simplify-path/
Notes:
    - use stack
'''
def simplifyPath(path: str) -> str:
    path_list = path.split('/')

    res = []
    for p in path_list:
        if p == '..':
            if res: res.pop()
        elif p not in ['.', '']:
            res.append(p)
    return '/' + '/'.join(res)

if __name__ == '__main__':
    p1 = "/home/"
    p2 = "/../"
    p3 = "/home//foo/"

    print(simplifyPath(p1))
    print(simplifyPath(p2))
    print(simplifyPath(p3))
