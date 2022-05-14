def decimal_binary(num):
    if num == 0:
        return ''
    rem = str(int(num % 2))
    return decimal_binary(int(num / 2)) + rem

if __name__ == '__main__':
    n1, n2 = 7, 4
    print(decimal_binary(n1))
    print(decimal_binary(n2))
