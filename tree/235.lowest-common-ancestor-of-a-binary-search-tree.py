#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''O(logn), get the two dfs stacks, then do a matching on the stack
    '''
    def __init__(self):
        self.stacks = []

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def binary_tree_search(root: 'TreeNode', node: 'TreeNode', stack: list):
            stack.append(root)
            if root.val == node.val:
                self.stacks.append(stack.copy())
                return
            if root.val < node.val:
                binary_tree_search(root.right, node, stack)
            else:
                binary_tree_search(root.left, node, stack)

        binary_tree_search(root, p, stack=[])
        binary_tree_search(root, q, stack=[])
        stack_p = self.stacks[0]
        stack_q = self.stacks[1]
        nodes_p_set = set([node.val for node in stack_p])
        for node in reversed(stack_q):
            if node.val in nodes_p_set:
                return node


class Solution:
    '''an elegant solution
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
       

# @lc code=end

