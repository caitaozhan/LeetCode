#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if root:
                if low <= root.val <= high:
                    self.ans += root.val
                    dfs(root.left)
                    dfs(root.right)
                elif root.val < low:
                    dfs(root.right)
                elif root.val > high:
                    dfs(root.left)

        self.ans = 0
        dfs(root)
        return self.ans

# @lc code=end

