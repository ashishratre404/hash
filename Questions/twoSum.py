# Leetcode: 1. Two Sum

# Apporach:
#     1. check if target - number exist in hashmap or not
#     2. if yes, then return its index from hashmap
#     3. if no then store the no. with its index to the hashmap.else

#             HashMap
#           value : index
#            5    :  0
#            2    :  1

class Solution:
    def twoSum(self, nums, target):
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


s = Solution()
print(s.twoSum([1,2,3,3,5,8,7], 9))