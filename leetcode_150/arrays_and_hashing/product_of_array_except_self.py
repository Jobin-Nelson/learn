from operator import mul
from itertools import starmap

def productExceptSelf(nums: list[int]) -> list[int]:
    N = len(nums)
    res = [1] * N

    prefix = 1
    for i in range(N):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(N-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

# def productExceptSelf(nums: list[int]) -> list[int]:
#     N = len(nums)
#     prefix_product = [1] * N
#     suffix_product = [1] * N
#     for i in range(1, N):
#         si = N - i - 1
#         prefix_product[i] = prefix_product[i-1] * nums[i-1]
#         suffix_product[si] = suffix_product[si+1] * nums[si+1]
#     print(f'{prefix_product=}')
#     print(f'{suffix_product=}')
#     # return list(starmap(mul, zip(prefix_product, suffix_product)))
#     return [p * s for p, s in zip(prefix_product, suffix_product)]

if __name__ == "__main__":
    i1 = [1,2,4,6]
    print(productExceptSelf(i1))
