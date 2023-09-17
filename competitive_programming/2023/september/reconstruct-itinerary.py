'''
Created Date: 2023-09-14
Qn: You are given a list of airline tickets where tickets[i] = [fromi, toi]
    represent the departure and the arrival airports of one flight. Reconstruct
    the itinerary in order and return it.

    All of the tickets belong to a man who departs from "JFK", thus, the
    itinerary must begin with "JFK". If there are multiple valid itineraries,
    you should return the itinerary that has the smallest lexical order when
    read as a single string.

        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order
        than ["JFK", "LGB"].

    You may assume all tickets form at least one valid itinerary. You must use
    all the tickets once and only once.
Link: https://leetcode.com/problems/reconstruct-itinerary/
Notes:
    - use dfs and adjacency list
'''
from collections import defaultdict

def findItinery(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    tickets.sort()
    for f, t in tickets:
        graph[f].append(t)

    res = ["JFK"]
    def dfs(src: str) -> bool:
        if len(res) == len(tickets) + 1: return True
        if src not in graph: return False

        temp = list(graph[src])
        for i, v in enumerate(temp):
            graph[src].pop(i)
            res.append(v)
            if dfs(v): return True
            graph[src].insert(i, v)
            res.pop()
        return False
    dfs("JFK")
    return res

if __name__ == '__main__':
    t1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    t2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

    print(findItinery(t1))
    print(findItinery(t2))
