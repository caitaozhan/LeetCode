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

    def flatten_helper(self, root):
        '''Given a root, flatten it and return the head and tail
        '''
        if root is None:
            return None, None
        
        left_head, left_tail = self.flatten_helper(root.left)
        right_head, right_tail = self.flatten_helper(root.right)
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


    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:                 # fail-2: forgot to check this
            return
        left_head, left_tail = self.flatten_helper(root.left)
        right_head, _ = self.flatten_helper(root.right)
        if left_head is None:
            pass
        elif left_head is not None and right_head is None:
            root.right = left_head
            root.left = None              # fail-1: forgot to None this
        elif left_head is not None and right_head is not None:
            root_right = root.right
            root.right = left_head
            root.left = None              # fail-1: forgot to None this
            left_tail.right = root_right


# @lc code=end

