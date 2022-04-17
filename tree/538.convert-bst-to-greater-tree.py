#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        # step 1: do inorder traverse
        inorder = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            inorder.append(cur.val)
            cur = cur.right

        # step 2: suffix array
        n = len(inorder)
        suffix = [0] * n
        suffix[n-1] = inorder[n-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] + inorder[i]

        # step 3: do inorder traverse again and change the node values
        index = 0
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur.val = suffix[index]
            index += 1
            cur = cur.right

        return root


class Solution:
    '''instead of doing two inorder traversal, do a reverse inorder traversal
    '''
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return None

        # do reverse inorder traverse
        summ = 0
        rinorder = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            summ += cur.val
            cur.val = summ
            cur = cur.left

        
# @lc code=end

