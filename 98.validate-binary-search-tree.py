#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (26.08%)
# Likes:    2671
# Dislikes: 387
# Total Accepted:    519.1K
# Total Submissions: 1.9M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
    
    def print(self):
        print(self.val, end=' ')

class Solution2:
    '''inorder the tree, check each node
    '''
    def __init__(self):
        self.answer = True

    def find_max(self, root):
        if root is None:
            return float('-inf')
        return max(self.find_max(root.left), root.val, self.find_max(root.right))

    def find_min(self, root):
        if root is None:
            return float('inf')
        return min(self.find_min(root.left), root.val, self.find_min(root.right))

    def preorder(self, root):
        if self.answer is False:
            return
        if root:
            left_max  = self.find_max(root.left)
            right_min = self.find_min(root.right)
            if left_max >= root.val or right_min <= root.val:
                self.answer = False
                return
            self.preorder(root.left)
            self.preorder(root.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self.preorder(root)
        return self.answer



class Solution:

    def helper(self, root, lower, upper):
        if root:
            if root.val <= lower or root.val >= upper:
                return False
            if not self.helper(root.left, lower, root.val):
                return False
            if not self.helper(root.right, root.val, upper):
                return False
        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, lower=float('-inf'), upper=float('inf'))


if __name__ == '__main__':
    pass

# @lc code=end



    # pre/in/post order by recursive

    # def isValidBST(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return []
    #     # preorder = [root.val] + self.isValidBST(root.left) + self.isValidBST(root.right)
    #     # inorder = self.isValidBST(root.left) + [root.val] + self.isValidBST(root.right)
    #     postorder = self.isValidBST(root.left) + self.isValidBST(root.right) + [root.val]
    #     for val in postorder:
    #         print(val, end=' ')
    #     print()
    #     return postorder



    # inorder by loop
    
    # stack = []
    # sol   = []
    # cur   = root
    # while stack or cur:
    #     while cur:
    #         stack.append(cur)
    #         cur = cur.left
    #     cur = stack.pop()
    #     sol.append(cur.val)
    #     cur = cur.right
    # for val in sol:
    #     print(val, end=' ')



    # preorder by loop

    # stack = []
    # sol   = []
    # cur   = root
    # while stack or cur:
    #     while cur:
    #         sol.append(cur.val)
    #         stack.append(cur)
    #         cur = cur.left
    #     cur = stack.pop()
    #     cur = cur.right
    # for val in sol:
    #     print(val, end=' ')



    # postorder by loop

    # stack = []
    # sol   = []
    # cur   = root
    # while stack or cur:
    #     while cur:
    #         sol.append(cur.val)
    #         stack.append(cur)
    #         cur = cur.right
    #     cur = stack.pop()
    #     cur = cur.left
    # sol.reverse()
    # for val in sol:
    #     print(val, end=' ')



    # postorder by loop

    # stack   = []
    # sol_r   = []  # solution reverse
    # stack.append(root)
    # while stack:
    #     cur = stack.pop()
    #     sol_r.append(cur.val)
    #     if cur.left:
    #         stack.append(cur.left)
    #     if cur.right:
    #         stack.append(cur.right)
    # sol_r.reverse()
    # sol = sol_r
    # for val in sol:
    #     print(val, end=' ')
