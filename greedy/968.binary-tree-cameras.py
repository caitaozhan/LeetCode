#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    '''O(nlogn), greedy approach, cover the tree from bottom up, only cover the deepest layer at a time
    '''
    def __init__(self):
        self.ans = 0
        self.deepest_depth = -1

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def mark(node):
            marked = False
            if node.val == 0:
                node.val = 1
                marked = True
            return marked

        def dfs(root, stack):
            if root:
                if len(stack) < self.deepest_depth:
                    dfs(root.left, stack + [root])
                    dfs(root.right, stack + [root])
                else:
                    if root.val == 1:
                        return
                    # reached the 'leaf' node, greedily put the camera on top of that leaf node
                    marked = False
                    rtn = mark(root)
                    marked = marked or rtn
                    if len(stack) >= 1:
                        rtn = mark(stack[-1])      # camera is at stack[-1]
                        marked = marked or rtn
                        if stack[-1].left:
                            rtn = mark(stack[-1].left)
                            marked = marked or rtn
                        if stack[-1].right:
                            rtn = mark(stack[-1].right)
                            marked = marked or rtn
                    if len(stack) >= 2:
                        rtn = mark(stack[-2])
                        marked = marked or rtn
                    if marked:
                        self.ans += 1

        def deepest(root, layer, upper):
            '''get the depth of the deepest non-marked node
            '''
            if root and layer <= upper:
                if root.val == 0:
                    self.deepest_depth = max(self.deepest_depth, layer)
                deepest(root.left, layer+1, upper)
                deepest(root.right, layer+1, upper)

        self.deepest_depth = -1
        deepest(root=root, layer=0, upper=float('inf'))
        while self.deepest_depth >= 0:  # keep marking node's value from 0 to 1 until every noded is marked
            dfs(root, stack=[])
            pre_deepest_depth = self.deepest_depth
            self.deepest_depth = -1
            deepest(root=root, layer=0, upper=pre_deepest_depth)
        return self.ans


class Solution:
    '''A more efficient greedy approach, also covering the tree from bottom up, but only doing DFS once
    '''
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        covered = set([None])

        def dfs(root, parent):
            if root:
                dfs(root.left, root)
                dfs(root.right, root)

                if (parent is None and root not in covered) or (root.left not in covered) or (root.right not in covered):
                   self.ans += 1
                   covered.update({root.left, root.right, root, parent})

        dfs(root, None)
        return self.ans




# @lc code=end

