#
# @lc app=leetcode id=669 lang=python3
#
# [669] Trim a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:

        def trim(root: list) -> Optional[TreeNode]:
            '''trim a root, return the trimmed root (the root itself may change)
            '''
            # fix the root if it is not a valid root
            while root:
                if low <= root.val <= high:
                    break
                elif root.val > high:
                    root = root.left
                else:  # root.val < low
                    root = root.right
            if not root:
                return None

            # trim left
            if root.left:
                if root.left.val >= low:
                    root.left = trim(root.left)
                else:  # root.left.val < low
                    if root.left.right:
                        root.left = trim(root.left.right)
                    else:
                        root.left = None
            # trim right
            if root.right:
                if root.right.val <= high:
                    root.right = trim(root.right)
                else:  # root.right.val > high
                    if root.right.left:
                        root.right = trim(root.right.left)
                    else:
                        root.right = None
            # return the root
            return root


        # step 1: find the new root, if necessary
        while root:
            if low <= root.val <= high:
                break
            elif root.val > high:
                root = root.left
            else:  # root.val < low
                root = root.right
        if not root:
            return None

        # step 2: trim left and right
        root.left = trim(root.left)
        root.right = trim(root.right)
        return root


# @lc code=end



[3,2,4,1]
2
4
[3,1,4,null,2]
3
4
[3,0,4,null,2,null,null,1]
1
3