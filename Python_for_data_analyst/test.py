def solution(number):
    threes = (number-1)//3
    fives = (number-1)//5
    fifteens = (number-1)//15
    return 3*threes*(threes+1)/2 + 5*fives*(fives+1)/2 - 15*fifteens*(fifteens+1)/2
    

