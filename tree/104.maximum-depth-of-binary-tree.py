#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (63.02%)
# Likes:    1895
# Dislikes: 63
# Total Accepted:    672.1K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    '''DFS, recursive funciton has no returns. from top to down
    '''
    def __init__(self):
        self.maxx = 0

    def dfs(self, root, level):
        '''
        Args:
            root -- 
            level -- current level
        '''
        if root is None:
            if level > self.maxx:
                self.maxx = level
            return
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

    def maxDepth(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.maxx


class Solution3:
    '''DFS, recursive function that returns something. from down to up
    '''
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution:
    '''Iterative, BFS
    '''
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        queue = [root]  # a queue for a level
        depth = 0
        while queue:
            depth += 1
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return depth


class Solution1:
    '''iterative, inorder
    '''
    def __init__(self):
        self.maxx = 0

    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = []
        cur = root
        level = 1
        maxx  = level
        while stack or cur:
            while cur:
                stack.append((cur, level))
                cur = cur.left
                level += 1
            cur, level = stack.pop()  # the node being put into inorder solution list
            maxx = max(maxx, level)
            cur = cur.right
            level += 1            
        return maxx

# @lc code=end

