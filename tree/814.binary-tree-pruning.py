#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''dfs for saving who shall be pruned
       bfs for pruning
    '''
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root) -> bool:
            '''return true if there is a 1 in the tree of root (include root)
            '''
            if root:
                left = helper(root.left)
                right = helper(root.right)
                if root.val == 0 and left is False and right is False:
                    prune.add(root)
                    return False
                else:
                    return True
            return False

        prune = set()
        helper(root)
        if root in prune:
            return None

        queue = [root]
        while queue:
            new_queue = []
            for node in queue:
                if node.left:
                    if node.left in prune:
                        node.left = None
                    else:
                        new_queue.append(node.left)
                if node.right:
                    if node.right in prune:
                        node.right = None
                    else:
                        new_queue.append(node.right)
            queue = new_queue
        return root



class Solution:
    '''only dfs
    '''
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root) -> bool:
            '''return true if there is a 1 in the tree of root (include root)
            '''
            if root:
                left = helper(root.left)
                right = helper(root.right)
                if left is False:
                    root.left = None
                if right is False:
                    root.right = None
                if root.val == 0 and left is False and right is False:
                    return False
                else:
                    return True
            return False

        ret = helper(root)
        if ret:
            return root
        else:            
            return None

# @lc code=end

