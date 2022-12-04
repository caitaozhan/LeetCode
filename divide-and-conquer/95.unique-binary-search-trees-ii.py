#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''divide and conquer
    '''
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def dfs(left_bound: int, right_bound: int) -> List[TreeNode]:
            '''the key is to return a list of tree root nodes
               left_bound and right_bound are inclusive
            '''
            if left_bound > right_bound:
                return [None]

            all_trees = []
            for val in range(left_bound, right_bound + 1):
                left_subtrees = dfs(left_bound, val - 1)
                right_subtrees = dfs(val + 1, right_bound)
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(val, left_subtree, right_subtree)
                        all_trees.append(root)
            return all_trees

        return dfs(1, n)

        

n = 3
s = Solution()
print(s.generateTrees(n))

# @lc code=end

