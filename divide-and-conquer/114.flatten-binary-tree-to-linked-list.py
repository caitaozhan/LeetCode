#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (45.23%)
# Likes:    1970
# Dislikes: 256
# Total Accepted:    283.4K
# Total Submissions: 624.7K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
# 
# For example, given the following tree:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 
# The flattened tree should look like:
# 
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def inorder(self, root):
        '''use for debug'''
        if root is None:
            return [None]
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def flatten_helper2(self, root):
        '''Given a root, flatten it and return the head and tail
        '''
        if root is None:
            return None, None
        
        left_head, left_tail = self.flatten_helper2(root.left)
        right_head, right_tail = self.flatten_helper2(root.right)
        if left_head is None and right_head is None:
            return root, root           # leaf node
        elif left_head is None and right_head is not None:
            return root, right_tail
        elif left_head is not None and right_head is None:
            root.right = left_head
            root.left = None             # fail-1: forgot to None this
            return root, left_tail
        elif left_head is not None and right_head is not None:
            root_right = root.right
            root.right = left_head
            root.left = None             # fail-1: forgot to None this
            left_tail.right = root_right
            return root, right_tail
        else:
            pass


    def flatten_helper(self, root):
        '''Given a root, flatten it and return the flattened list's tail (the flattened list's head is the root itself)
        '''
        if root is None:
            return None
        
        left_tail = self.flatten_helper(root.left)
        right_tail = self.flatten_helper(root.right)
        if root.left is None and root.right is None:
            return root
        elif root.left is None and root.right is not None:
            return right_tail
        elif root.left is not None and root.right is None:
            root.right = root.left
            root.left = None
            return left_tail
        elif root.left is not None and root.right is not None:
            root_right = root.right
            root.right = root.left
            root.left = None
            left_tail.right = root_right
            return right_tail
        else:
            pass


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flatten_helper(root)


class Solution:
    '''7/29/2022 redo
    '''
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten_helper(root) -> "TreeNode":
            '''flatten the tree (root and its subtree), and return the flattened tree's tail node
            '''
            if root is None:
                return None
            
            left_tail  = flatten_helper(root.left)
            right_tail = flatten_helper(root.right)
            
            if left_tail and right_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
                return right_tail
            elif left_tail and right_tail is None:
                root.right = root.left
                root.left = None
                return left_tail
            elif left_tail is None and right_tail:
                return right_tail
            else:
                return root
                
        flatten_helper(root)

# @lc code=end

