#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''divide and conquer
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


class Solution:
    '''dfs
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(root):
            if root is None:
                return
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans


class Solution:
    '''using a stack, iterative
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                ans.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return ans


class Solution:
    '''using a stack, iterative
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
        return ans

# @lc code=end

