#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.ans = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(root):
            if self.ans is not None:
                return

            if root:
                if root.val == target.val:
                    self.ans = root
                    return
                
                if root.left:
                    dfs(root.left)
                if root.right:
                    dfs(root.right)
                
        dfs(cloned)
        return self.ans


class Solution:
    '''comparing the reference is faster than comparing the values that the reference points at
    '''

    def __init__(self):
        self.ans = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        def dfs(o_root, c_root):
            if self.ans is not None:
                return

            if o_root:
                if o_root == target:
                    self.ans = c_root
                    return
                
                if o_root.left:
                    dfs(o_root.left, c_root.left)
                if o_root.right:
                    dfs(o_root.right, c_root.right)
                
        dfs(original, cloned)
        return self.ans

# @lc code=end

