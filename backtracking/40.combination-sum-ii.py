#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

from typing import List
from collections import Counter

# @lc code=start

class Solution:
    '''TLE
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(stack, i, summation):
            '''summation is the summation from the 0th to (i-1)th element
            '''
            if i < len(candidates) - 1 and summation + suffixsum[i] < target:   # prune
                return
            if summation > target:
                return
            if summation == target:
                tup = tuple(stack)
                if tup not in ans:
                    ans.add(tup)
                return
            if i == len(candidates):
                return
            
            # select the current ith element
            dfs(stack + [candidates[i]], i + 1, summation + candidates[i])

            # skip the current ith element
            dfs(stack, i + 1, summation)
        
        candidates.sort()
        n = len(candidates)
        suffixsum = [0] * n
        suffixsum[-1] = candidates[-1]
        for i in range(n-2, -1, -1):
            suffixsum[i] = suffixsum[i + 1] + candidates[i]

        ans = set()
        dfs(stack=[], i=0, summation=0)
        ans = [list(item) for item in ans]
        return ans


class Solution:
    '''Use a Counte to decrease the length of the recursion stack
    '''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(stack, i, summation):
            '''summation is the summation from the 0th to (i-1)th element
            '''
            if summation > target:
                return
            if summation == target:
                ans.append(stack.copy())
                return
            if i == len(candidates):
                return
            
            # skip the current ith element
            dfs(stack, i + 1, summation)
            
            # select the current num with some repetation
            num, count = candidates[i]
            for repeat in range(1, count + 1):
                stack.append(num)
                dfs(stack, i + 1, summation + num * repeat)
            
            last = stack[-1]
            while stack and stack[-1] == last:
                stack.pop()

            # code is simpler, but more time, because of more time spent in copying
            # for repeat in range(1, count + 1):
            #     # select the current ith element (num) count number of times.
            #     dfs(stack + [num] * repeat, i + 1, summation + num * repeat)
        
        mycount = Counter(candidates)
        candidates = [(num, count) for num, count in sorted(mycount.items())]

        ans = []
        dfs(stack=[], i=0, summation=0)
        return ans


candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(len(candidates))
target = 27

candidates = [1,1]
target=2

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(len(candidates))
target = 30

# candidates = [10,1,2,7,6,1,5]
# target = 8

s = Solution()
print(s.combinationSum2(candidates, target))


# @lc code=end

