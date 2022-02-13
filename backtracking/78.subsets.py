#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

from typing import List
from itertools import combinations
from copy import deepcopy

# @lc code=start
class Solution1:
    '''using itertools.combinations'''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            ans.extend(list(combinations(nums, i)))
        return ans
    
class Solution2:
    '''cascading, it is like DP, there is subproblem, but no min or max going on (keep all subproblems) '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            new = [tmp + [num] for tmp in ans]
            ans.extend(new)
        return ans

class Solution:
    '''dfs, stopping criteria is reaching end of nums'''
    def __init__(self):
        self.ans = []
        self.nums = None

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(stack, i):
            if i == len(self.nums):
                self.ans.append(stack.copy())
                return

            dfs(stack, i + 1)                    # do not pick ith element
            dfs(stack + [self.nums[i]], i + 1)   # pick the ith element
            # the below three lines are equivalent to the above single line
            # stack.append(self.nums[i])
            # dfs(stack, i + 1)
            # stack.pop()
    
        self.nums = nums
        stack = []
        dfs(stack, 0)
        return self.ans


class Solution:
    '''dfs, stopping criteria is length of subset'''
    def __init__(self):
        self.ans = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(stack, first):
            if len(stack) == k:
                self.ans.append(stack.copy())
                return

            for i in range(first, len(nums)):
                # use nums[i] in the combination
                stack.append(nums[i])
                dfs(stack, i + 1)
                # do not use nums[i] in the combination
                stack.pop()
    
        stack = []
        for k in range(len(nums) + 1):
            dfs(stack, 0)
        return self.ans

if __name__=='__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
# @lc code=end

