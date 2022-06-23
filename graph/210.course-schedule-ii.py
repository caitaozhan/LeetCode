#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (37.17%)
# Likes:    1402
# Dislikes: 96
# Total Accepted:    194.8K
# Total Submissions: 522.2K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
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

# @lc code=start
class Solution:
    '''topological sort by kahn's algorithm
    '''
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for prereq in prerequisites:
            b, a = prereq     # a --> b
            adjlist[a].append(b)
            indegree[b] += 1

        stack = []
        for i, indeg in enumerate(indegree):
            if indeg == 0:
                stack.append(i)

        topolo = []
        while stack:
            a = stack.pop()
            topolo.append(a)
            for b in adjlist[a]:
                indegree[b] -= 1
                if indegree[b] == 0:
                    stack.append(b)

        if len(topolo) == numCourses:
            return topolo
        else:
            return []


# @lc code=end

