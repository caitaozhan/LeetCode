#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
class Solution:
    '''pick the median
    '''
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        median = nums[len(nums)//2]
        ans = 0
        for num in nums:
            ans += abs(num - median)
        return ans
        
# @lc code=end

