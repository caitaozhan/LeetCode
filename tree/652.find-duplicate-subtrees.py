#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import Optional, List

class Solution:
    '''if Null node is included, then preorder traversal is unique (postorder also unique)
       let's use the preorder traversal as a "hash" to a subtree 
    '''
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def preorder(root: Optional[TreeNode]) -> str:
            if root is None:
                return '()'
            
            root_str = '(' + str(root.val) + ')'
            left_str  = preorder(root.left)
            right_str = preorder(root.right)

            subtree_str = root_str + left_str + right_str  # preorder and postorder are correct, inorder is not
            dd[subtree_str].append(root)
            return subtree_str
        
        dd = defaultdict(list)
        preorder(root)
        ans = []
        for key, val in dd.items():
            if len(val) >= 2:
                ans.append(val[0])
        return ans



        
# @lc code=end

