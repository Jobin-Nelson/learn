# Write a program to check if the given string is a palindrome. 
# Ensure that any valid python string can be handled by your program

#Ex: 
#- amma - Palindrome
#- Madam - Palindrome
#- Malayalam - Palindrome
#- 1234321 - Palindrome
#- Madam, I'm Adam!! - Palindrome 

def main(s: str) -> bool:
    stack = []

    hashmap = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    for c in s:
        if c in hashmap:
            if stack and stack[-1] == hashmap[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False
    
if __name__ == '__main__':
    s1, s2, s3 = "()", "()[]{}", "()[](])]"
    print(main(s1))
    print(main(s2))
    print(main(s3))