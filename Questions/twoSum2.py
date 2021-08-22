# Leetcode: 167. Two sum II - Input array is sorted

# Approach:
#     1. Array is sorted
#     2. start with two pointer one at start and one from end
#     3. if sum of two pointer becomes bigger than target then decrease right pointer by one(because we have to decrease the sum)
#     4. if sum if lesser then increase left pointer by one (we have to increase the sum)
#     5. if equall then return [l+1, r+1], (pluse one, because array is one based indexed)

class Solution:
    def twosum(self, numbers, target):
        l, r = 0, len(numbers) -1

        while l < r:
            tot = numbers[l] + numbers[r]

            if tot > target:
                r -= 1
            elif tot < target:
                l += 1
            else:
                return [l+1, r+1]
        return []