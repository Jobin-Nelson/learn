def is_palindrome(word):
    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])

    return False

if __name__ == '__main__':
    print(is_palindrome('racecar'))
    print(is_palindrome('kayak'))
    print(is_palindrome('malayalam'))
    print(is_palindrome('not a palindrome'))

