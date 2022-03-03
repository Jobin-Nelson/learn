def sum_of_num(num):
    if num <= 1:
        return num
    return num + sum_of_num(num-1)

if __name__ == '__main__':
    print(sum_of_num(10))
    print(sum_of_num(6))
