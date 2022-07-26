#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.stack_p = []
        self.stack_q = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, stack):
            '''dfs -- preorder traversal
            '''
            if root:
                stack.append(root)

                if root == p:
                    self.stack_p = stack.copy()
                if root == q:
                    self.stack_q = stack.copy()
                if self.stack_p and self.stack_q:
                    return
                
                if root.left:
                    dfs(root.left, stack)
                    stack.pop()
                if root.right:
                    dfs(root.right, stack)
                    stack.pop()

        stack = []
        dfs(root, stack)
        
        set_p = set()
        for node in self.stack_p:
            set_p.add(node.val)
        
        ans = None
        while self.stack_q:
            node = self.stack_q.pop()
            if node.val in set_p:
                ans = node
                break
        
        return ans




        
# @lc code=end

