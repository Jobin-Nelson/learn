'''
Created Date: 19-06-2022
Qn: You are given an array of strings products and a string searchWord.
    Design a system that suggests at most three product names from products after 
    each character of searchWord is typed. Suggested products should have common prefix 
    with searchWord. If there are more than three products with a common prefix return 
    the three lexicographically minimums products.
    Return a list of lists of the suggested products after each character of 
searchWord is typed.
Link: https://leetcode.com/problems/search-suggestions-system/
Notes:
- once sorted use two pointers to return the answer
'''
def suggestedProducts(products: list[str], searchWord: str) -> list[list[str]]:
    res = []
    products.sort()

    l, r = 0, len(products) -1 
    for i in range(len(searchWord)):
        c = searchWord[i]
        while l <= r and (len(products[l]) <= i or products[l][i] != c):
            l += 1
        while l <= r and (len(products[r]) <= i or products[r][i] != c):
            r -= 1

        res.append([])
        remain = r - l + 1
        for j in range(min(3, remain)):
            res[-1].append(products[l + j])
    return  res

if __name__ == '__main__':
    p1, s1 = ["mobile","mouse","moneypot","monitor","mousepad"], 'mouse'
    p2, s2 = ["havana"], 'havana'
    p3, s3 = ["bags","baggage","banner","box","cloths"], 'bags'
    print(suggestedProducts(p1, s1))
    print(suggestedProducts(p2, s2))
    print(suggestedProducts(p3, s3))
