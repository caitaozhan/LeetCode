#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(32):
            if 3 ** i == n:
                return True
        return False


import math

class Solution:
    '''O(1) time
    '''
    def isPowerOfThree(self, n: int) -> bool:
        i = math.log(n, 3)
        if 3 ** int(i) == n or 3 ** (int(i) + 1) == n:
            return True
        return False


n = 0
s = Solution()
print(s.isPowerOfThree(n))

# @lc code=end

