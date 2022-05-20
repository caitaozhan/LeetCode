#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(root) -> int:
            '''return the length of the longest univalue path that includes the current root node'''
            if root:
                left, right = 0, 0
                if root.left:
                    if root.left.val != root.val:
                        left = 0
                        dfs(root.left)
                    else:
                        left = dfs(root.left) + 1
                if root.right:
                    if root.right.val != root.val:
                        right = 0
                        dfs(root.right)
                    else:
                        right = dfs(root.right) + 1
                self.ans = max(left + right, self.ans)
                return max(left, right)
            else:
                return 0
        
        dfs(root)
        return self.ans

        
# @lc code=end

