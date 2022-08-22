#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or (n != 1 and n % 2 == 1):
            return False

        for x in range(32):
            if n == 4 ** x:
                return True
                
        return False
        
# @lc code=end

