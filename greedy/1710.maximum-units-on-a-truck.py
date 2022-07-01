#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        ans = 0
        for num, unit in boxTypes:
            if num < truckSize:
                ans += num * unit
                truckSize -= num
            else:
                ans += truckSize * unit
                break
        return ans

        
# @lc code=end

