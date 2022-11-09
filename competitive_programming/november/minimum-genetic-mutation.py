'''
Created Date: 2022-11-02
Qn: A gene string can be represented by an 8-character long string, with
    choices from 'A', 'C', 'G', and 'T'.

    Suppose we need to investigate a mutation from a gene string start to a
    gene string end where one mutation is defined as one single character
    changed in the gene string.

    - For example, "AACCGGTT" --> "AACCGGTA" is one mutation. 

    There is also a gene bank bank that records all the valid gene mutations. A
    gene must be in bank to make it a valid gene string.

    Given the two gene strings start and end and the gene bank bank, return the
    minimum number of mutations needed to mutate from start to end. If there is
    no such a mutation, return -1.

    Note that the starting point is assumed to be valid, so it might not be
    included in the bank.
Link: https://leetcode.com/problems/minimum-genetic-mutation/
Notes:
    - bfs to find the min number of mutations needed
    - same as word ladder
'''
from collections import deque

def minMutation(start: str, end: str, bank: list[str]) -> int:
    N = len(start)
    bank = set(bank)
    if end not in bank: return -1

    q = deque()
    q.append((start, 0))
    visited = set()

    while q:
        gene, mutation = q.popleft()
        if gene == end: return mutation

        for i in range(N):
            for letter in 'ATCG':
                new_gene = gene[:i] + letter + gene[i+1:]
                if new_gene not in visited and new_gene in bank:
                    q.append((new_gene, mutation+1))
                    visited.add(new_gene)
    return -1

if __name__ == '__main__':
    s1, e1, b1 = "AACCGGTT", "AACCGGTA", ["AACCGGTA"]
    s2, e2, b2 = "AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]
    s3, e3, b3 = "AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]

    print(minMutation(s1, e1, b1))
    print(minMutation(s2, e2, b2))
    print(minMutation(s3, e3, b3))
