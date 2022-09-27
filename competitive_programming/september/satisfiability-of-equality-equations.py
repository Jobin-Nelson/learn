'''
Created Date: 2022-09-26
Qn: You are given an array of strings equations that represent relationships
    between variables where each string equations[i] is of length 4 and takes one
    of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
    letters (not necessarily different) that represent one-letter variable names.

    Return true if it is possible to assign integers to variable names so as to
    satisfy all the given equations, or false otherwise.
Link: https://leetcode.com/problems/satisfiability-of-equality-equations/
Notes:
    - use undirected graph
    - try to connect parents
    - check if all the not equals doesn't have the same parent
'''
def equationsPossible(equations: list[str]) -> bool:
    parent, diff = {}, []

    def find(x):
        if x not in parent: return x
        else: return find(parent[x])

    for s in equations:
        a, b = s[0], s[3]

        if s[1] == '=':
            x, y = find(a), find(b)
            if x != y: parent[y] = x
        else:
            diff.append((a, b))

    return all(find(a) != find(b) for a, b in diff)

if __name__ == '__main__':
    e1, e2 = ["a==b", "b!=a"], ["b==a", "a==b"]

    print(equationsPossible(e1))
    print(equationsPossible(e2))
