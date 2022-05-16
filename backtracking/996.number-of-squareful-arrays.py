#
# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#

from typing import List
from collections import defaultdict, Counter
import math

# @lc code=start
class Solution:
    '''no need for a set
    '''
    def __init__(self):
        self.ans = 0

    def is_perfect_square(self, num):
        sqrt = int(math.sqrt(num))
        return sqrt**2 == num

    def numSquarefulPerms(self, nums: List[int]) -> int:
        # step 1: build the graph
        nums_counter = Counter(nums)
        keys = list(nums_counter.keys())
        valid_pair = []
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                if self.is_perfect_square(keys[i] + keys[j]):
                    valid_pair.append((keys[i], keys[j]))
        graph = defaultdict(list)
        for a, b in valid_pair:
            if a != b:
                graph[a].append(b)
                graph[b].append(a)
            if a == b:
                graph[a].append(b)
        
        # step 2: check if all connected
        for node, neigh in graph.items():
            if len(neigh) == 0:
                return 0
        
        # step 3: do backtracking
        def dfs(cur, nums_counter, stack):
            nums_counter[cur] -= 1
            stack.append(cur)
            if len(stack) == len(nums):
                self.ans += 1

            for neigh in graph[cur]:
                if nums_counter[neigh] > 0:
                    dfs(neigh, nums_counter, stack)

            stack.pop()
            nums_counter[cur] += 1
        
        for start in graph.keys():
            dfs(start, nums_counter.copy(), stack=[])
        
        return self.ans
        

nums = [1,1,8,1,8]
s = Solution()
print(s.numSquarefulPerms(nums))

# @lc code=end

