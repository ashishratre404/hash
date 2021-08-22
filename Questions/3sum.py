# Leetcode: 15. 3Sum

# Approach:
#   Note: bruteforce will take O(n3), so
#   0. sort array 
#   1. choose first element and then for remaining two element apply two pointer (see two sum II, leetcode: 167)

class Solution:
    def threesum(self, nums):
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l<r:
                        l += 1
        return res
