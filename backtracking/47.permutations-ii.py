#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

from typing import List
from collections import Counter

# @lc code=start
class Solution:
    '''a simple adaption to the original permutation problem 46
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(visited, stack):
            if len(stack) == len(nums):
                tmp = tuple(stack)
                if tmp not in ans:
                    ans.add(tmp)

            for i in range(len(visited)):
                if visited[i] == 0:
                    visited[i] = 1
                    backtrack(visited, stack + [nums[i]])
                    visited[i] = 0

        ans = set()
        visited = [0] * len(nums)
        backtrack(visited, stack = [])
        ans = [list(x) for x in ans]
        return ans


class Solution:
    '''a smarter adaption to the original permutation problem 46
       instead of using a visited arry, use a counter
    '''
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(counter, stack):
            if len(stack) == len(nums):
                ans.append(stack.copy())
            
            for num in counter.keys():
                if counter[num] > 0:
                    counter[num] -= 1
                    backtrack(counter, stack + [num])
                    counter[num] += 1

        ans = []
        counter = Counter(nums)
        stack = []
        backtrack(counter, stack)
        return ans



# @lc code=end

