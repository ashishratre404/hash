# Leetcode: 202. Happy Number

# how will we get digits of numbers:
#  then 1. mod of 10 will give digit of unit place
#       2. modify no. by dividing it by 10 (it will remove digit of unit place)

# for 91
# 91 % 10 = 1 (1 is digit of unit place)
# 91 // 10 = 9 ( this will remove 1 from 91)

class Solution:
    def isHappy(self, n):
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.helper(n)

            if n == 1:
                return True
        return False
        
    def helper(self, n):
        output = 0 
        while n:
            digit = n % 10
            digit = digit * digit
            output += digit
            n = n//10
        return output
