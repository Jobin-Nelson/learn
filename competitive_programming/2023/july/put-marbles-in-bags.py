'''
Created Date: 2023-07-08
Qn: You have k bags. You are given a 0-indexed integer array weights where
    weights[i] is the weight of the ith marble. You are also given the integer
    k.

    Divide the marbles into the k bags according to the following rules:

        - No bag is empty. 
        - If the ith marble and jth marble are in a bag, then all marbles with
          an index between the ith and jth indices should also be in that same
          bag.
        - If a bag consists of all the marbles with an index from i to j
          inclusively, then the cost of the bag is weights[i] + weights[j].

    The score after distributing the marbles is the sum of the costs of all the
    k bags.

    Return the difference between the maximum and minimum scores among marble
    distributions.
Link: https://leetcode.com/problems/put-marbles-in-bags/
Notes:
    - calculate the pair_weights of all adjacent weights
    - sort and get the min and max sum of k-1 (since there are k-1 splits) pair_weights
'''
def putMarbles(weights: list[int], k: int) -> int:
    N = len(weights)
    pair_weights = [weights[i] + weights[i+1] for i in range(N-1)]
    pair_weights.sort()

    res = sum(pair_weights[N-2-i] - pair_weights[i] for i in range(k-1))
    # res = 0
    # for i in range(k-1):
    #     res += pair_weights[N-2-i] + pair_weights[i]
    return res


if __name__ == '__main__':
    w1, k1 = [1,3,5,1], 2
    w2, k2 = [1,3], 2

    print(putMarbles(w1, k1))
    print(putMarbles(w2, k2))
