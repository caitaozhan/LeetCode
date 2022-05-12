#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

from typing import List

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(visited, stack):
            if len(stack) == len(nums):
                ans.append(stack.copy())

            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    dfs(visited, stack + [nums[i]])
                    visited[i] = 0

        ans = []
        visited = [0] * len(nums)
        dfs(visited, stack = [])
        return ans

nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))

# @lc code=end

