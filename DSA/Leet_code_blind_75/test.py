def two_sum(nums, target):
    hashmap = {}

    for i, n in enumerate(nums):
        complement = target - n
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[n] = i

if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    nums2 = [3, 2, 4]
    target2 = 6
    print(two_sum(nums1, target1))
    print(two_sum(nums2, target2))
