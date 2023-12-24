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
    - use hashmaps and heaps
"""
import heapq
from collections import defaultdict
from typing import Self


class Food:
    def __init__(self, name: str, rating: int):
        self.food_name = name
        self.food_rating = rating

    def __lt__(self, other: Self) -> bool:
        if self.food_rating == other.food_rating:
            return self.food_name < other.food_name
        return self.food_rating > other.food_rating


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_rating = {}
        self.food_cuisine = {}
        self.cuisine_food = defaultdict(list)
        for i in range(len(foods)):
            self.food_rating[foods[i]] = ratings[i]
            self.food_cuisine[foods[i]] = cuisines[i]
            heapq.heappush(self.cuisine_food[cuisines[i]], Food(foods[i], ratings[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.food_rating[food] = newRating
        heapq.heappush(self.cuisine_food[cuisine], Food(food, newRating))

    def highestRated(self, cuisine: str) -> str:
        highest_rated = self.cuisine_food[cuisine][0]
        while self.food_rating[highest_rated.food_name] != highest_rated.food_rating:
            heapq.heappop(self.cuisine_food[cuisine])
            highest_rated = self.cuisine_food[cuisine][0]
        return highest_rated.food_name

    # def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
    #     self.lookup = defaultdict(list)
    #     self.clookup = {foods[i]: cuisines[i] for i in range(len(foods))}
    #     for i, cuisine in enumerate(cuisines):
    #         heapq.heappush(self.lookup[cuisine], (-ratings[i], foods[i]))
    #
    # def changeRating(self, food: str, newRating: int) -> None:
    #     cuisine = self.clookup[food]
    #     for i, (_, f) in enumerate(self.lookup[cuisine]):
    #         if f == food:
    #             self.lookup[cuisine][i] = (-newRating, food)
    #             heapq.heapify(self.lookup[cuisine])
    #             break
    #
    # def highestRated(self, cuisine: str) -> str:
    #     return heapq.heappop(self.lookup[cuisine])[1]


if __name__ == "__main__":
    f = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    )
    print(f.highestRated("korean"))
    print(f.highestRated("japanese"))
    f.changeRating("sushi", 16)
    print(f.highestRated("japanese"))
    f.changeRating("ramen", 16)
    print(f.highestRated("japanese"))
