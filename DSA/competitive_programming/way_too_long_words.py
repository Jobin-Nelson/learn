n = int(input())

words = []
for i in range(n):
    words.append(input())

for i, word in enumerate(words):
    if len(word) > 10:
        res = word[0] + str(len(word[1:-1])) + word[-1]
    else:
        res = word
    print(res)
