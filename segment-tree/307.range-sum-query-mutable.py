#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

from typing import List


class SegTreeNode:
    def __init__(self, low: int, high: int, summ: int, left: "SegTreeNode", right: "SegTreeNode"):
        self.low = low
        self.high = high
        self.summ = summ         # the summation of elements nums[low ... high] (inclusive)
        self.left = left         # left child
        self.right = right       # right child

class SegTree:
    def __init__(self, nums):
        self._root = self._build_tree(0, len(nums)-1, nums)
    
    def _build_tree(self, low: int, high: int, nums: list) -> SegTreeNode:
        if low == high:
            return SegTreeNode(low, high, nums[low], None, None)    # leaf node
        mid = (low + high) // 2
        left = self._build_tree(low, mid, nums)
        right = self._build_tree(mid+1, high, nums)
        summ = left.summ + right.summ
        return SegTreeNode(low, high, summ, left, right)

    def update(self, index: int, val: int):
        self._update(self._root, index, val)

    def _update(self, root: SegTreeNode, index: int, val: int):
        if root.low == root.high == index:
            root.summ = val                   # leaf node
            return
        mid = (root.low + root.high) // 2
        if index <= mid:
            self._update(root.left, index, val)
        else:
            self._update(root.right, index, val)
        root.summ = root.left.summ + root.right.summ

    def sum_range(self, low: int, high: int) -> int:
        return self._sum_range(self._root, low, high)

    def _sum_range(self, root: SegTreeNode, low: int, high: int):
        if low == root.low and high == root.high:
            return root.summ
        mid = (root.low + root.high) // 2
        if high <= mid:
            return self._sum_range(root.left, low, high)
        elif low > mid:
            return self._sum_range(root.right, low, high)
        else:
            return self._sum_range(root.left, low, mid) + self._sum_range(root.right, mid+1, high)
        

# @lc code=start
class NumArray:
    '''segment tree'''
    def __init__(self, nums: List[int]):
        self._segtree = SegTree(nums)
        
    def update(self, index: int, val: int) -> None:
        self._segtree.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self._segtree.sum_range(left, right)


# Your NumArray object will be instantiated and called as such:

nums = [1, 2, 3, 4, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
print(obj.sumRange(1, 3))
obj.update(1, 5)
print(obj.sumRange(0, 2))
print(obj.sumRange(1, 3))

# @lc code=end

