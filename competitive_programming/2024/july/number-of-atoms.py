"""
Created Date: 2024-07-14
Qn: Given a string formula representing a chemical formula, return the count of
    each atom.

    The atomic element always starts with an uppercase character, then zero or
    more lowercase letters, representing the name.

    One or more digits representing that element's count may follow if the
    count is greater than 1. If the count is 1, no digits will follow.

    - For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible. 

    Two formulas are concatenated together to produce another formula.

    - For example, "H2O2He3Mg4" is also a formula. 

    A formula placed in parentheses, and a count (optionally added) is also a
    formula.

    - For example, "(H2O2)" and "(H2O2)3" are formulas. 

    Return the count of all elements as a string in the following form: the
    first name (in sorted order), followed by its count (if that count is more
    than 1), followed by the second name (in sorted order), followed by its
    count (if that count is more than 1), and so on.

    The test cases are generated so that all the values in the output fit in a
    32-bit integer.
Link: https://leetcode.com/problems/number-of-atoms/
Notes:
"""
class Solution
    def countAtoms(self, formula: str) -> str:
        stack = []
        self.count = {}
        self.index = 1
        def next_number() -> int:
            start = self.index
            while self.index < len(formula) and formula[self.index].isdigit():
                self.index += 1
            return int(formula[start:self.index])
        def next_element() -> str:
            start = self.index
            while self.index < len(formula) and formula[self.index].isalpha():
                self.index += 1
            return formula[start:self.index]
        def next_token() -> dict[str, int]:
            count = {}
            if formula[self.index].isupper():
                element = next_element()
                if formula[self.index].isdigit():
                    count[element] = int

        def dfs(l: int) -> dict[str,int]:
            sub_formula = formula[l:self.index]
            count= {}
            while self.index < len(sub_formula):
                if sub_formula[self.index].isupper():
                    
                elif sub_formula[self.index].isdigit():
                    m = self.index
                    while self.index < len(sub_formula) and sub_formula[self.index].isdigit():
                        self.index += 1
                    count[sub_formula[l:m]] = int(sub_formula[m:self.index])
                elif sub_formula[self.index] == ')':
                    if stack:
                        start = stack.pop()
                        c = dfs(start)
                        for k, v in c.items():
                            count[k] += v * 
                elif sub_formula[self.index] == '(':
                    stack.append(self.index)
                self.index += 1

if __name__ == '__main__':
    f1 = "H2O"
    f2 = "Mg(OH)2"
    f3 = "K4(ON(SO3)2)2"

    print(Solution().countAtoms(f1))
    print(Solution().countAtoms(f2))
    print(Solution().countAtoms(f3))
