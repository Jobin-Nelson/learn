'''
Qn: Return the answers to all queries. If a single answer cannot be determined, return -1.0.
Link: https://leetcode.com/problems/evaluate-division/
Notes:
- graph problem use adjacency list with dict as values
'''
def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
    # creating adjacency list
    adj = {}
    for (a, b), v in zip(equations, values):
        if a not in adj: adj[a] = {}
        if b not in adj: adj[b] = {}
        adj[a][b] = v
        adj[b][a] = 1/v

    res = []
    # finding ans to queries through recursion
    def dfs(x, y, visited):
        if x not in adj or y not in adj: return -1

        if y in adj[x]:
            return adj[x][y]

        for i in adj[x]:
            if i not in visited:
                visited.add(i)
                output = dfs(i, y, visited)
                if output == -1:
                    continue
                else:
                    return output * adj[x][i]
        return -1

    for p, q in queries:
        res.append(dfs(p, q, set()))

    # finding ans to queries through iteration
    #for a, b in queries:
        #if a in adj and b in adj:
            #for val in adj[a]:
                #if val == b:
                    #res.append(adj[a][b])
                    #break
                #elif val in adj[b]:
                    #res.append(adj[a][val] * (1/adj[b][val]))
                    #break
            #else:
                #res.append(-1)
        #else:
            #res.append(-1)
    return res

if __name__ == '__main__':
    e1, v1, q1 = [["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    e2, v2, q2 = [["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    e3, v3, q3 = [["a","b"]], [0.5],  [["a","b"],["b","a"],["a","c"],["x","y"]]
    print(calcEquation(e1, v1, q1))
    print(calcEquation(e2, v2, q2))
    print(calcEquation(e3, v3, q3))

