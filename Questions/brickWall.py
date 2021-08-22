# Leetcode: 554. Brick Wall
class Solution:
    def leastBricks(self, wall):
        countGap = { 0 : 0 }  # position : no. of brick gaps

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)
                # print(countGap)
            
        return len(wall) - max(countGap.values())


s = Solution()
print(s.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1],[6]]))