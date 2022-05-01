'''
Qn: Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character
Link: https://leetcode.com/problems/backspace-string-compare/
Notes:
- use stack to push and pop on #, check both stacks are same
- two pointer going l <- r, skipping on # and checking 
'''
def backspace_compare(s: str, t: str) -> bool:
    ns , nt = [], []
    for c in s:
        if ns and c == '#':
            ns.pop()
        elif c != '#':
            ns.append(c)

    for c in t:
        if nt and c == '#':
            nt.pop()
        elif c != '#':
            nt.append(c)

    return ns == nt

def backspace_compare_two_pointer(s: str, t: str) -> bool:
    sp, tp = len(s)-1, len(t)-1
    s_skip = t_skip = 0

    while sp >= 0 or tp >= 0:
        while sp >= 0:
            if s[sp] == '#':
                sp -= 1
                s_skip += 1
            elif s_skip:
                sp -= 1
                s_skip -= 1
            else:
                break
        while tp >= 0:
            if t[tp] == '#':
                tp -= 1
                t_skip += 1
            elif t_skip:
                tp -= 1
                t_skip -= 1
            else:
                break
        if sp >= 0 and tp >= 0 and s[sp] != t[tp]:
            return False
        if (sp >= 0) != (tp >= 0):
            return False
        sp -= 1
        tp -= 1
    return True


if __name__ == '__main__':
    s1, t1 = 'ab#c', 'ad#c'
    s2, t2 = 'ab##', 'c#d#'
    s3, t3 = 'a#c', 'b'
    print(backspace_compare(s1, t1))
    print(backspace_compare(s2, t2))
    print(backspace_compare(s3, t3))

    print(backspace_compare_two_pointer(s1, t1))
    print(backspace_compare_two_pointer(s2, t2))
    print(backspace_compare_two_pointer(s3, t3))
