"""
Created Date: 2023-12-15
Qn: You are given the array paths, where paths[i] = [cityAi, cityBi] means
    there exists a direct path going from cityAi to cityBi. Return the destination
    city, that is, the city without any path outgoing to another city.

    It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.
Link: https://leetcode.com/problems/destination-city/
Notes:
"""


def destCity(paths: list[list[str]]) -> str:
    out_going_set = set(path[0] for path in paths)
    for _, b in paths:
        if b not in out_going_set:
            return b


if __name__ == "__main__":
    p1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    p2 = [["B", "C"], ["D", "B"], ["C", "A"]]
    p3 = [["A", "Z"]]

    print(destCity(p1))
    print(destCity(p2))
    print(destCity(p3))
