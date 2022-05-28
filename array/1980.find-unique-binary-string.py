#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        n = len(nums[0])
        for i in range(2**n):
            s = bin(i)[2:]
            if len(s) < n:
                s = '0'*(n-len(s)) + s
            if i < len(nums):
                if s != nums[i]:
                    return s
            else:
                return s

        
# @lc code=end

