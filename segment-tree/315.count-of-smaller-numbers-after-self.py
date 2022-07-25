#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
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

    def update(self, index: int):
        self._update_increment(self._root, index)

    def _update_increment(self, root: SegTreeNode, index: int):
        if root.low == root.high == index:
            root.summ += 1                   # leaf node
            return
        mid = (root.low + root.high) // 2
        if index <= mid:
            self._update_increment(root.left, index)
        else:
            self._update_increment(root.right, index)
        root.summ = root.left.summ + root.right.summ

    def sum_range(self, low, high) -> int:
        if low <= high:
            return self._sum_range(self._root, low, high)
        else:
            return 0

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
class Solution:
    '''segment tree + bucket sort like idea (put numbers in a bucket)
       TLE
    '''
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums2 = [0] * (2*10**4 + 1)
        offset = 10**4
        ans = [0] * len(nums)
        segtree = SegTree(nums2)
        for i in range(len(nums)-1, -1, -1):
            index = nums[i] + offset
            segtree.update(index)
            ans[i] = segtree.sum_range(low=0, high=index-1)
        return ans

class Solution:
    '''segment tree + bucket sort like idea (put numbers in a bucket)
       instead of a fixed nums2 with 2*10**4 + 1 elements, 
       use a nums2 whose length depends on the max and min value of nums
    '''
    def countSmaller(self, nums: List[int]) -> List[int]:
        minn = min(nums)
        maxx = max(nums)
        nums2 = [0] * (maxx - minn + 1)
        offset = -minn
        ans = [0] * len(nums)
        segtree = SegTree(nums2)
        for i in range(len(nums)-1, -1, -1):
            index = nums[i] + offset
            segtree.update(index)
            ans[i] = segtree.sum_range(low=0, high=index-1)
        return ans

nums = [5,2,2,6,1]
print(len(nums))
s = Solution()
print(s.countSmaller(nums))

# @lc code=end

