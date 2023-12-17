"""
Created Date: 2023-12-17
Qn: Design a food rating system that can do the following:

        - Modify the rating of a food item listed in the system. 
        - Return the highest-rated food item for a type of cuisine in the
          system.

    Implement the FoodRatings class:

        - FoodRatings(String[] foods, String[] cuisines, int[] ratings)
          Initializes the system. The food items are described by foods,
          cuisines and ratings, all of which have a length of n. 
            - foods[i] is the name of the ith food, 
            - cuisines[i] is the type of cuisine of the ith food, and
            - ratings[i] is the initial rating of the ith food. 
        - void changeRating(String food, int newRating) Changes the rating of
          the food item with the name food. 
        - String highestRated(String cuisine) Returns the name of the food item
          that has the highest rating for the given type of cuisine. If there
          is a tie, return the item with the lexicographically smaller name.

    Note that a string x is lexicographically smaller than string y if x comes
    before y in dictionary order, that is, either x is a prefix of y, or if i
    is the first position such that x[i] != y[i], then x[i] comes before y[i]
    in alphabetic order.
Link: https://leetcode.com/problems/design-a-food-rating-system/
Notes:
"""


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        pass

    def changeRating(self, food: str, newRating: int) -> None:
        pass

    def highestRated(self, cuisines: str) -> str:
        pass


if __name__ == "__main__":
    f = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    )
    print(f.highestRated("korean"))
    print(f.highestRated("japanese"))
    print(f.highestRated("sushi"))
    print(f.changeRating("sushi", 16))
    print(f.highestRated("japanese"))
    print(f.changeRating("ramen", 16))
    print(f.highestRated("japanese"))
