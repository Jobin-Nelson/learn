import time

def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number+1

try :
    num = int(input("Type in any integer : ")) # Ask for a number
    while num!=1:
        num = collatz(num)
        print(num)
        time.sleep(0.1)
except ValueError: 
    print("Enter an integer, not a word.")
    