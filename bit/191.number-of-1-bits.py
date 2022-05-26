#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += n % 2
            n >>= 1
        return ans

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            if n & 1:
                ans += 1
            n >>= 1
        return ans

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        mask = 1
        for _ in range(32):
            if n & mask != 0:
                ans += 1
            mask <<= 1
        return ans


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            ans += 1
            n &= (n - 1)
        return ans


# @lc code=end

