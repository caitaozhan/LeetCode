#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (55.21%)
# Likes:    6654
# Dislikes: 162
# Total Accepted:    587.3K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given two integer arrays preorder and inorder where preorder is the preorder
# traversal of a binary tree and inorder is the inorder traversal of the same
# tree, construct and return the binary tree.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.
# 
# 
#

from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''travere in preorder (explicitly)
       build one node (the root) at a time in each recursive call
       the recursive function return the root
    '''
    def __init__(self):
        self.i = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(left, right):
            if left > right:   # the left node
                return None
            
            root_val = preorder[self.i]
            root = TreeNode(root_val)
            self.i += 1  # to the next one in the preorder

            indx = mydict[root_val]
            root.left = helper(left, indx - 1)
            root.right = helper(indx + 1, right)
            return root

        mydict = {}
        for i, val in enumerate(inorder):
            mydict[val] = i
        self.i = 0
        root = helper(left=0, right=len(preorder)-1)
        return root



class Solution:
    '''traverse in preorder (but implicitly)
       prebuild all the nodes, then connect them
       the recursive function returns None
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_node2index = {}
        for i, node in enumerate(inorder):
            in_node2index[node] = i
        nodes = []
        for node in preorder:
            nodes.append(TreeNode(node))
        
        def build(pre_low: int, pre_up: int, in_low, in_up):
            '''
            Args:
                pre_low  -- the low pointer in the preorder
                pre_high -- the high pointer in the preorder
                in_low   -- the low pointer in the corresponding inorder
                in_high  -- the high pointer in the corresponding inorder
            Return: None
            '''
            if pre_low > pre_up:
                return

            root = nodes[pre_low]
            in_rootindex = in_node2index[root.val]
            
            leftchilds_num = in_rootindex - in_low
            if leftchilds_num > 0:
                root.left = nodes[pre_low + 1]
                build(pre_low + 1, pre_low + leftchilds_num, in_low, in_rootindex-1)  # root's left childs
            
            rightchilds_num = in_up - in_rootindex
            if rightchilds_num > 0:
                root.right = nodes[pre_low + leftchilds_num + 1]
                build(pre_low + leftchilds_num + 1, pre_up, in_rootindex+1, in_up)    # root's right childs

        build(0, len(preorder)-1, 0, len(inorder)-1)

        return nodes[0]

# @lc code=end

