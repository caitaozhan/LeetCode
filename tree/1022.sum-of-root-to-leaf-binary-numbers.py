#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (66.26%)
# Likes:    678
# Dislikes: 74
# Total Accepted:    57K
# Total Submissions: 82.1K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
# 
# Return the sum of these numbers.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''using a stack to record the recursion path
    '''
    def __init__(self):
        self.ans = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = []
        self.dfs(root, stack)
        return self.ans
        
    def dfs(self, root, stack):
        if root is None:
            return
        if root.left is None and root.right is None:
            stack.append(root.val)
            self.ans += self.stack2number(stack)
            stack.pop()
            return
        
        stack.append(root.val)
        self.dfs(root.left, stack)
        self.dfs(root.right, stack)
        stack.pop()
            
    def stack2number(self, stack):
        s = ''.join(map(str, stack))
        num = int(s, 2)
        return num


class SolutionString:
    '''using a string to record the recursion path. comparint to the stack, this don't need to pop()
       becuase passing a parameter is shallow copy. when the parameter is a integer, it copies the value
       when pasing a list, it is passing a pointer to the list, and the list can be modified
    '''
    def __init__(self):
        self.ans = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        string = ""
        self.dfs(root, string)
        return self.ans
        
    def dfs(self, root, string):
        if root is None:
            return
        if root.left is None and root.right is None:
            string += str(root.val)
            self.ans += int(string, 2)
            return

        string += str(root.val)
        self.dfs(root.left, string)
        self.dfs(root.right, string)

# @lc code=end

