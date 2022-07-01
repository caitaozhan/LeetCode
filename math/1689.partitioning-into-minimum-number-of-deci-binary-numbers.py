#
# @lc app=leetcode id=1689 lang=python3
#
# [1689] Partitioning Into Minimum Number Of Deci-Binary Numbers
#

# @lc code=start
class Solution:
    '''the answer is the largest digit in the number
    '''
    def minPartitions(self, n: str) -> int:
        ans = '0'
        for ch in n:
            if ch > ans:
                ans = ch
        return ans


# @lc code=end

