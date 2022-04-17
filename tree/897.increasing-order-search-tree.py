#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        cur = root
        prev = None
        new_root = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev is None:
                new_root = cur
            else:
                prev.left = None
                prev.right = cur
            prev = cur
            cur = cur.right
        prev.left = None

        return new_root
            
        
# @lc code=end
