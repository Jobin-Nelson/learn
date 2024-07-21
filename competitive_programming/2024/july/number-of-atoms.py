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
    - use parsing technique
"""
from collections import defaultdict

class Solution:
    def countAtoms(self, formula: str) -> str:
        self.index = 0
        def next_number() -> int:
            count = 1
            start = self.index
            while self.index < len(formula) and formula[self.index].isdigit():
                self.index += 1
            if formula[start:self.index]:
                count = int(formula[start:self.index])
            return count
        def next_element() -> str:
            start = self.index
            self.index += 1
            while self.index < len(formula) and formula[self.index].islower():
                self.index += 1
            return formula[start:self.index]

        stack = [defaultdict(int)]
        while self.index < len(formula):
            while self.index < len(formula):
                if formula[self.index] == '(':
                    self.index += 1
                    stack.append(defaultdict(int))
                elif formula[self.index] == ')':
                    self.index += 1
                    cur_map = stack.pop()
                    prev_map = stack[-1]
                    count = next_number()
                    for k, v in cur_map.items():
                        prev_map[k] += v * count
                else:
                    element = next_element()
                    count = next_number()
                    cur_map = stack[-1]
                    cur_map[element] += count
        return ''.join(f'{k}{v}' if v > 1 else k for k, v in sorted(stack[-1].items(), key=lambda x: x[0]))

if __name__ == '__main__':
    f1 = "H2O"
    f2 = "Mg(OH)2"
    f3 = "K4(ON(SO3)2)2"

    print(Solution().countAtoms(f1))
    print(Solution().countAtoms(f2))
    print(Solution().countAtoms(f3))
