#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

from typing import List

# @lc code=start
class Solution:
    '''use a set to prevent duplicates
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()

        def dfs(stack, i):
            if i == len(nums):
                ans.add(tuple(stack.copy()))
                return
            dfs(stack, i + 1)
            dfs(stack + [nums[i]], i + 1)
        
        nums.sort()
        dfs([], 0)
        ans = [list(item) for item in ans]
        return ans



class Solution:
    '''classic backtrack, prevent backtrack during recursion
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(stack, idx):
            ans.append(stack.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: # in this current level,
                    continue                           # prevent duplicate by only selecting one element if multiple same exists
                backtrack(stack + [nums[i]], i + 1)
        
        nums.sort()
        ans = []
        backtrack([], 0)
        return ans

# @lc code=end

