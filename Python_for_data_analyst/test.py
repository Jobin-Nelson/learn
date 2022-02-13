def balancedSums(arr):
    # Write your code here
    length = len(arr)
    
    pre = [0] * length
    post = [0] * length
    if length > 2:
        for i in range(length-1):
            pre[i+1] = arr[i] + pre[i]
            post[length-i-2] = arr[length-i-1] + post[length-i-1]
                
        i = 0
        print(pre)
        print(post)
        while i < length:
            if post[i] == pre[i]:
                return 'YES'
            i += 1
    return 'NO'

if __name__ == '__main__':
    arr = [1, 2, 3, 3]
    arr_1 = [1, 2, 3]
    print(balancedSums(arr))
    print(balancedSums(arr_1))
