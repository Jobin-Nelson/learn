'''
Created Date: 2023-02-09
Qn: You are given an array of strings ideas that represents a list of names to
    be used in the process of naming a company. The process of naming a company is
    as follows:

    Choose 2 distinct names from ideas, call them ideaA and ideaB. 
    Swap the first letters of ideaA and ideaB with each other. 
    If both of the new names are not found in the original ideas, then the name
    ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is
    a valid company name. 

    Otherwise, it is not a valid name. Return the number of distinct valid
    names for the company.
Link: https://leetcode.com/problems/naming-a-company/
Notes:
    - group ideas by initials
    - res += 2 * (suffixes not in b) * (suffixes not in a)
'''
def distinctNames(ideas: list[str]) -> int:
    initial_groups = [set() for _ in range(26)]

    for idea in ideas:
        initial_groups[ord(idea[0]) - ord('a')].add(idea[1:])

    res = 0
    for i in range(25):
        for j in range(i+1, 26):
            num_of_mutual = len(initial_groups[i] & initial_groups[j])
            res += 2 * (len(initial_groups[i]) - num_of_mutual) * (len(initial_groups[j]) - num_of_mutual)
    return res
    
if __name__ == '__main__':
    i1 = ["coffee","donuts","time","toffee"]
    i2 = ["lack","back"]

    print(distinctNames(i1))
    print(distinctNames(i2))
