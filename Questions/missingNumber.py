# leetcode: 268. Missing Number

# Given: fist N no. with one no. missing
#  [1,2,3,5] find missing no.? 
#  here missing no. is 4

#  Approach
#  (sum of first N no.) - (sum of given list of no.)


class Solution:
    def missingNumber(self, nums):
        n = max(nums)
        res = 0
        for i in nums:
            res += i
        
        return ((n*(n+1))//2) - res

s = Solution()
print(s.missingNumber([1,2,4]))