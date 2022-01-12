import pandas as pd


# Vim is super useful oh yeah baby
    df = pd.DataFrame(data=[[1,2,3]],columns=['ones','two','three'])

df.head(10)
'Hello' world!

def two_sum(nums: List[int], target: int)-> List[int]:
    hashmap = {}
    for i, num in enumerate(nums):
        complement  = target - num
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i