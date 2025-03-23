"""
Created Date: 2025-03-21
Qn: You have information about n different recipes. You are given a string
    array recipes and a 2D string array ingredients. The ith recipe has the
    name recipes[i], and you can create it if you have all the needed
    ingredients from ingredients[i]. A recipe can also be an ingredient for
    other recipes, i.e., ingredients[i] may contain a string that is in
    recipes.

    You are also given a string array supplies containing all the ingredients
    that you initially have, and you have an infinite supply of all of them.

    Return a list of all the recipes that you can create. You may return the
    answer in any order.

    Note that two recipes may contain each other in their ingredients.
Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
Notes:
    - treat the problem as a graph problem
    - use dfs
"""

import unittest


class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        can_cook = {s: True for s in supplies}
        recipe_index = {r: i for i, r in enumerate(recipes)}

        def dfs(r: str) -> bool:
            if r in can_cook:
                return can_cook[r]
            if r not in recipe_index:
                return False
            can_cook[r] = False
            if any(not dfs(nei) for nei in ingredients[recipe_index[r]]):
                return False
            can_cook[r] = True
            return True

        return [r for r in recipes if dfs(r)]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_findAllRecipes1(self):
        r = ["bread"]
        i = [["yeast", "flour"]]
        s = ["yeast", "flour", "corn"]
        expected = ["bread"]
        self.assertEqual(expected, self.sol.findAllRecipes(r, i, s))

    def test_findAllRecipes2(self):
        r = ["bread", "sandwich"]
        i = [["yeast", "flour"], ["bread", "meat"]]
        s = ["yeast", "flour", "meat"]
        expected = ["bread", "sandwich"]
        self.assertEqual(expected, self.sol.findAllRecipes(r, i, s))

    def test_findAllRecipes3(self):
        r = ["bread", "sandwich", "burger"]
        i = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]]
        s = ["yeast", "flour", "meat"]
        expected = ["bread", "sandwich", "burger"]
        self.assertEqual(expected, self.sol.findAllRecipes(r, i, s))

    def test_findAllRecipes4(self):
        r = [
            "xevvq",
            "izcad",
            "p",
            "we",
            "bxgnm",
            "vpio",
            "i",
            "hjvu",
            "igi",
            "anp",
            "tokfq",
            "z",
            "kwdmb",
            "g",
            "qb",
            "q",
            "b",
            "hthy",
        ]
        i = [
            ["wbjr"],
            ["otr", "fzr", "g"],
            ["fzr", "wi", "otr", "xgp", "wbjr", "igi", "b"],
            ["fzr", "xgp", "wi", "otr", "tokfq", "izcad", "igi", "xevvq", "i", "anp"],
            ["wi", "xgp", "wbjr"],
            ["wbjr", "bxgnm", "i", "b", "hjvu", "izcad", "igi", "z", "g"],
            ["xgp", "otr", "wbjr"],
            ["wbjr", "otr"],
            ["wbjr", "otr", "fzr", "wi", "xgp", "hjvu", "tokfq", "z", "kwdmb"],
            ["xgp", "wi", "wbjr", "bxgnm", "izcad", "p", "xevvq"],
            ["bxgnm"],
            ["wi", "fzr", "otr", "wbjr"],
            ["wbjr", "wi", "fzr", "xgp", "otr", "g", "b", "p"],
            ["otr", "fzr", "xgp", "wbjr"],
            ["xgp", "wbjr", "q", "vpio", "tokfq", "we"],
            ["wbjr", "wi", "xgp", "we"],
            ["wbjr"],
            ["wi"],
        ]
        s = ["wi", "otr", "wbjr", "fzr", "xgp"]
        expected = [
            "xevvq",
            "izcad",
            "bxgnm",
            "i",
            "hjvu",
            "tokfq",
            "z",
            "g",
            "b",
            "hthy",
        ]
        self.assertEqual(expected, self.sol.findAllRecipes(r, i, s))


if __name__ == '__main__':
    unittest.main()
