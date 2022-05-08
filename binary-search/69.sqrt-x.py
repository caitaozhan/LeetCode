#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low < high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid
            else:
                low = mid + 1
        if low * low > x:   # made some bugs here...
            return low - 1
        else:
            return low
        
# @lc code=end

