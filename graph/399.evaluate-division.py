#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (50.88%)
# Likes:    2683
# Dislikes: 218
# Total Accepted:    148.4K
# Total Submissions: 281.1K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# You are given equations in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating-point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
# 
# Example 1:
# 
# 
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# 
# 
# Example 2:
# 
# 
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# 
# 
# Example 3:
# 
# 
# Input: equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= equations[i][0], equations[i][1] <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= queries[i][0], queries[i][1] <= 5
# equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of
# lower case English letters and digits.
# 
# 
#

# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    '''build a graph and do dfs
    '''
    def __init__(self):
        self.g = None
        self.prod = 0
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (a, b), w in zip(equations, values):
            g[a].append((b, w))
            g[b].append((a, 1/w))
        self.g = g
        ans = []
        for a, b in queries:
            self.prod = -1
            if a in self.g and b in self.g:
                visited = set()
                prod = 1
                self.prod = -1
                self.dfs(a, b, visited, prod)
            ans.append(self.prod)
        return ans
    
    def dfs(self, cur, target, visited, prod):
        if self.prod != -1:
            return
        visited.add(cur)
        if cur == target:
            self.prod = prod
            return
        for nxt, w in self.g[cur]:
            if nxt not in visited:
                self.dfs(nxt, target, visited, prod*w)

class Solution2:
    '''Another way of doing dfs using a return value
       I prefer using an outside value instead of return value
    '''
    def __init__(self):
        self.g = None
    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (a, b), w in zip(equations, values):
            g[a].append((b, w))
            g[b].append((a, 1/w))
        self.g = g
        ans = []
        for a, b in queries:
            factor = -1
            if a in self.g and b in self.g:
                visited = set()
                prod = 1
                factor = self.dfs(a, b, visited, prod)
            ans.append(factor)
        return ans
    
    def dfs(self, cur, target, visited, prod):
        visited.add(cur)
        if cur == target:
            return prod
        ret = -1
        for nxt, w in self.g[cur]:
            if nxt not in visited:
                ret = self.dfs(nxt, target, visited, prod*w)
                if ret != -1:
                    break
        return ret


class Solution3:
    '''no return value, no member using self., but using a list that pass into the parameter
    '''
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dfs(cur, end, cost, visited, final_cost):
            if final_cost:
                return
            if cur == end:
                final_cost.append(cost)
                return
            visited.add(cur)
            for nxt, val in graph[cur]:
                if nxt not in visited:
                    dfs(nxt, end, cost*val, visited, final_cost)
        
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1/v))
            
        ans = []
        for a, b in queries:
            if a not in graph:
                ans.append(-1.0)
                continue
            if a == b:
                ans.append(1.0)
                continue
            final_cost = []
            visited = set()
            dfs(a, b, 1, visited, final_cost)
            value = final_cost[0] if final_cost else -1
            ans.append(value)
        return ans


equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
values = [3.0,4.0,5.0,6.0]
queries = [["x2","x4"]]
# queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]

s = Solution()
print(s.calcEquation(equations, values, queries))

# @lc code=end

