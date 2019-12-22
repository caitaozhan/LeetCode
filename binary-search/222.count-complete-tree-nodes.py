#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (35.57%)
# Likes:    1401
# Dislikes: 160
# Total Accepted:    162.1K
# Total Submissions: 415.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.countNodes(root.left) + 1 + self.countNodes(root.right)


class Solution:
    '''utilize the properties of the complete binary tree
    '''
    def count_level(self, root):
        counter = 0
        while root:
            root = root.left
            counter += 1
        return counter - 1  # the leaf node do not count
    
    def exist(self, root, mid, level):
        '''see if a node mid exists on the last level
        '''
        mid_binary = bin(mid)[2:]
        delta = level - len(mid_binary)
        if delta > 0:
            mid_binary = '0'*delta + mid_binary
        cur = root
        for b in mid_binary:
            if b == '0':
                cur = cur.left
            else:
                cur = cur.right
        return cur is not None

    def countNodes(self, root: TreeNode) -> int:
        level = self.count_level(root)
        if level < 0:
            return 0
        elif level == 0:
            return 1

        first_part = 2**(level) - 1

        left, right = 0, 2**(level) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.exist(root, mid, level):
                left = mid + 1
            else:
                right = mid - 1
        second_part = right + 1
        return first_part + second_part
        
# @lc code=end

