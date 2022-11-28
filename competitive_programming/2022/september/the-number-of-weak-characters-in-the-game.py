'''
Created Date: 2022-09-09
Qn: You are playing a game that contains multiple characters, and each of the
    characters has two main properties: attack and defense. You are given a 2D
    integer array properties where properties[i] = [attacki, defensei] represents
    the properties of the ith character in the game.

    A character is said to be weak if any other character has both attack and
    defense levels strictly greater than this character's attack and defense
    levels. More formally, a character i is said to be weak if there exists another
    character j where attackj > attacki and defensej > defensei.

    Return the number of weak characters.
Link: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
Notes:
    - sort attack in descending with defence in ascending
    - count everytime defence is less than the cur_max_defence
'''
def numberOfWeakCharacters(properties: list[list[int]]) -> int:
    properties.sort(reverse=True)
    result = max_defence = 0
    for _, defence in properties:
        if defence < max_defence:
            result += 1
        else:
            max_defence = defence
    return result


if __name__ == '__main__':
    p1 = [[5, 5], [6, 3], [3, 6]]
    p2 = [[2, 2], [3, 3]]
    p3 = [[1, 5], [10, 4], [4, 3]]

    print(numberOfWeakCharacters(p1))
    print(numberOfWeakCharacters(p2))
    print(numberOfWeakCharacters(p3))
