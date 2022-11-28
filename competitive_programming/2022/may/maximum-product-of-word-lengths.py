'''
Qn: Given a string array words, return the maximum value of 
    length(word[i]) * length(word[j]) where the two words do not share common letters. 
    If no such two words exist, return 0.
Link: https://leetcode.com/problems/maximum-product-of-word-lengths/
Notes:
    - detect no common letters using set.isdisjoint() method
'''
def maxProduct(words: list[str]) -> int:
    lookup = { word: set(word) for word in words }
    max_len = 0
    for i in words:
        for j in words:
            if lookup[i].isdisjoint(lookup[j]):
                max_len = max(max_len, len(i) * len(j))
    return max_len
            
if __name__ == '__main__':
    w1 = ["abcw","baz","foo","bar","xtfn","abcdef"]
    w2 = ["a","ab","abc","d","cd","bcd","abcd"]
    w3 = ["a","aa","aaa","aaaa"]
    print(maxProduct(w1))
    print(maxProduct(w2))
    print(maxProduct(w3))
