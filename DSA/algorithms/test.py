def locate_card(numbers, query):
    l, r = 0, len(numbers)-1

    while l <= r:
        m = (r+l)//2
        if numbers[m] < query:
            l = m+1
        elif numbers[m] > query:
            r = m-1
        else:
            if (m-1 >= 0) and (numbers[m-1] == query):
                r = m-1
            else:
                return m

    return -1

if __name__ == '__main__':
    print('located the card at', locate_card([1, 4, 6, 7, 8, 9], 7))
    print('located the card at', locate_card([1, 2, 3, 4, 5, 5, 5, 5, 6], 5))
    print('located the card at', locate_card([1, 1, 2, 3, 4, 5, 5, 5, 5, 6], 1))
