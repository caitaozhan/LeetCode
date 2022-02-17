#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

from typing import List

# @lc code=start
class Solution:
    '''backtracking'''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i, stack, summation):
            if summation > target:
                return
            if i == len(candidates):
                if summation == target:
                    ans.append(stack.copy())
                return
            
            # repeat current's ith element
            stack.append(candidates[i])
            dfs(i, stack, summation + candidates[i])

            # go to the next element
            stack.pop()
            dfs(i+1, stack, summation)

        ans = []
        dfs(i=0, stack=[], summation=0)
        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))

    candidates = [2, 3, 5]
    target = 8
    s = Solution()
    print(s.combinationSum(candidates, target))

# @lc code=end

