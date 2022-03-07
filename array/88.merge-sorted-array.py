#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

from collections import deque
from typing import List

# @lc code=start
class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        time:  O(m + n)
        space: O(m)
        using a queue... how did I come up with this? ...
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return

        queue = deque([nums1[0]])
        i = j = 0
        while i < m and j < n:
            if queue[0] <= nums2[j]:
                nums1[i] = queue.popleft()
                i += 1
                if i < m:
                    queue.append(nums1[i])
            else:
                nums1[i] = nums2[j]
                i += 1
                j += 1
                if i < m:
                    queue.append(nums1[i])
        while i < m:
            # now nums2 is done, nums1 is not
            nums1[i] = queue.popleft()
            i += 1
            if i < m:
                queue.append(nums1[i])
        
        while i < m + n:
            if len(queue) == 0:
                nums1[i] = nums2[j]
                j += 1
                i += 1
            elif j == n:
                nums1[i] = queue.popleft()
                i += 1
            else:
                if queue[0] <= nums2[j]:
                    nums1[i] = queue.popleft()
                    i += 1
                else:
                    nums1[i] = nums2[j]
                    i += 1
                    j += 1


class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        time:  O(m + n)
        space: O(m)
        """
        nums1_copy = nums1[:m]
        i = j = k = 0
        while i < m and j < n:
            if nums1_copy[i] <= nums2[j]:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if i < m:
            nums1[k:] = nums1_copy[i:]
        else:
            nums1[k:] = nums2[j:]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        time:  O(m + n)
        space: O(1)
        The idea is to start from the end of nums1, instead of traditionally starting from the beginning
        """
        p1 = m - 1
        p2 = n - 1
        for i in range(m + n - 1, -1, -1):
            if p1 < 0:
                nums1[:i+1] = nums2[:p2+1]
                break
            if p2 < 0:
                break
            if nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1
            else:
                nums1[i] = nums1[p1]
                p1 -= 1




if __name__ == '__main__':
    # a = [1,2,3,0,0,0]
    # m = 3
    # b = [2,5,6]
    # n = 3

    # a = [1,2,3,4,0,0,0,0]
    # m = 4
    # b = [5,6,7,8]
    # n = 4

    # a = [3,4,7,8,0,0,0,0]
    # m = 4
    # b = [1,2,5,6]
    # n = 4

    # a = [1,2,4,5,6,0]
    # m = 5
    # b = [3]
    # n = 1

    a = [2,0]
    m = 1
    b = [1]
    n = 1

    s = Solution()
    s.merge(a, m, b, n)
    print(a)

# @lc code=end

