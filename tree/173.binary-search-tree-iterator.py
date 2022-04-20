#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        while self.stack or self.cur:
            while self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            self.cur = self.stack.pop()
            ret = self.cur.val
            self.cur = self.cur.right
            return ret

    def hasNext(self) -> bool:
        if self.stack or self.cur:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

