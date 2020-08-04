#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#
# https://leetcode.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (38.95%)
# Likes:    1610
# Dislikes: 75
# Total Accepted:    167.2K
# Total Submissions: 422.6K
# Testcase Example:  '[1,3,null,null,2]'
#
# Two elements of a binary search tree (BST) are swapped by mistake.
# 
# Recover the tree without changing its structure.
# 
# Example 1:
# 
# 
# Input: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# Output: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# Output: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 
# Follow up:
# 
# 
# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?
# 
# 
#

from typing import List

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    '''if a tree is a binary search tree, then its inorder traversal is sorted
    '''
    def inorder(self, root: TreeNode):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def find_misplaced(self, inorder: List):
        misplaced = []
        for i in range(len(inorder)-1):
            if inorder[i] > inorder[i+1]:
                misplaced.append(inorder[i])
                misplaced.append(inorder[i+1])
        return misplaced[0], misplaced[-1]

    def traverse_swap(self, root: TreeNode, u, v):
        if not root:
            return
        if root.val == u:
            root.val = v
        elif root.val == v:
            root.val = u
        self.traverse_swap(root.left, u, v)
        self.traverse_swap(root.right, u, v)

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = self.inorder(root)
        u, v = self.find_misplaced(inorder)
        self.traverse_swap(root, u, v)


class Solution:
    '''using iteration instead of recursion (Solution2), and traverse only once
    '''
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        misplaced = []
        stack = []
        cur = root
        pre = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            
            if pre:
                if pre.val > cur.val:
                    misplaced.append(pre)
                    misplaced.append(cur)
            pre = cur

            cur = cur.right

        x, y = misplaced[0], misplaced[-1]
        x.val, y.val = y.val, x.val

        

# @lc code=end

