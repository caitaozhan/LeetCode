#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (40.05%)
# Likes:    2532
# Dislikes: 128
# Total Accepted:    294.4K
# Total Submissions: 733.1K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#

from typing import List
from collections import defaultdict

# @lc code=start
class SolutionTS:
    '''Topological sort solution
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for prereq in prerequisites:
            b, a = prereq   # a --> b
            adjlist[a].append(b)
            indegree[b] += 1
        
        stack = []  # store nodes that has zero indegree
        for i, indeg in enumerate(indegree):
            if indeg == 0:
                stack.append(i)  # find the initial courses

        while stack:
            a = stack.pop()
            for b in adjlist[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    stack.append(b)
        
        for indeg in indegree:  # check if there is any nodes with some amount of indegree
            if indeg != 0:
                return False
        return True

class Solution:
    '''Strongly Connected Component Solution
    '''
    def __init__(self):
        self.graph = None
        self.graph_reverse = None

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:  # b --> a
            graph[b].append(a)
        self.graph = graph
        visited = [0] * numCourses
        stack   = []

        # step 1: do a dfs, store the node's post number of the DFS in increasing order
        for i in range(numCourses):
            if visited[i] == 0:
                self.dfs(i, visited, stack)
        
        # step 2: reverse the graph
        graph_r = defaultdict(list)
        for a, b in prerequisites:
            graph_r[a].append(b)
        self.graph_reverse = graph_r

        # step 3: do a dfs on the reversed graph in the order of stack, we get SCC, 
        # if the number of the nodes in a CC > 1, then there is a cycle, then return False
        visited = [0] * numCourses
        while stack:
            start = stack.pop()
            if visited[start] == 0:
                scc = []
                self.dfs2(start, visited, scc)
                if len(scc) > 1:
                    return False
        return True

    def dfs2(self, i, visited, scc):
        visited[i] = 1
        scc.append(i)
        for nxt in self.graph_reverse[i]:
            if visited[nxt] == 0:
                self.dfs2(nxt, visited, scc)

    def dfs(self, i, visited, stack):
        visited[i] = 1
        for nxt in self.graph[i]:
            if visited[nxt] == 0:
                self.dfs(nxt, visited, stack)
        stack.append(i)   # append here

    

# @lc code=end
