#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    ''' divide and conquer
    '''
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


class Solution:
    ''' dfs
    '''
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(root):
            if root is None:
                return
            
            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)
        
        dfs(root)
        return ans


class Solution:
    '''using a stack, iterative, a reverse of preorder
    '''
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                ans.append(cur.val)
                cur = cur.right    # reverse of preorder
            cur = stack.pop()
            cur = cur.left         # reverse of preorder
        return reversed(ans)       # reverse


# @lc code=end

