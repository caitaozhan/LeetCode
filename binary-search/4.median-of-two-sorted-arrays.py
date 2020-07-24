#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (26.98%)
# Likes:    5390
# Dislikes: 795
# Total Accepted:    544.6K
# Total Submissions: 2M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

from typing import List

'''
My first attemp failed. I tried doing binary search on both arrays...
The correct way of doing it is doing binary search on one of the arrays, preferably the smaller one, 
and directly get the pointer on the second array by using the condition of median

My second attemp also failed...
Failed dealing with corner cases, my way of dealing with edge conditions is too complicated. 
Too complicated usually means something (not good) is going on. Good solutions should be relatively elegant.
I have some issues dealing with index-1 and zero index stuff.
'''

# @lc code=start
"""
class SolutionFail:

    @staticmethod
    def check(nums1, mid1, nums2, mid2):
        '''check whether every element on the left side is smaller than the right side of both arrays'''
        if mid1 >= 1 and mid2 >= 1:
            if nums1[mid1 - 1] <= nums2[mid2] and nums2[mid2 - 1] <= nums1[mid1]:
                return True
            else:
                return False
        else:  # this also indicates that the binary search should end
            return True
    
    @staticmethod
    def move_left_pointer(nums1, mid1, nums2, mid2):
        ''' whether the left pointer should move towards right direction
        '''
        # note that the index here are safe, checked by the Solution.check
        print(nums1[mid1 - 1], nums2[mid2], nums2[mid2 - 1], nums1[mid1])
        if nums1[mid1 - 1] < nums2[mid2]:
            return True
        else:
            return False

    @staticmethod
    def get_median(nums1, mid1, nums2, mid2, left, right):
        iseven = True if (len(nums1)+len(nums2))%2 == 0 else False
        if mid1 >= 1 and mid2 >= 1 and left <= right:  # there is a good partition
            if iseven:
                median = (max(nums1[mid1 - 1], nums2[mid2 - 1]) + min(nums1[mid1], nums2[mid2])) / 2
            else:
                median = min(nums1[mid1], nums2[mid2])
        elif mid1 == 0:
            half = (len(nums1) + len(nums2)) // 2
            if iseven:
                if half == len(nums1):
                    median = (nums1[mid1] + nums2[mid2]) / 2
                else:  # half > len(nums1) --> lens(nums2) > half
                    median = (nums2[half] + nums2[half + 1]) / 2
            else: # is odd
                median = nums2[half + 1] 
        elif mid1 == len(nums1) - 1:
            half = (len(nums1) + len(nums2)) // 2
            if iseven:
                if half == len(nums1):
                    median = (nums1[mid1] + nums2[mid2]) / 2
                else:
                    median = (nums2[-half] + nums2[-half-1]) / 2
            else:
                median = nums2[-half-1]
        return median

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1    # make nums1 the smaller size list
        half = (len(nums1) + len(nums2)) // 2
        left, right = 0, len(nums1) - 1
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1             # do later out of bound? looks safe
            # the left side is  nums1[0 .. mid1 - 1] and nums2[0 .. mid2 - 1]
            # the right side is nums1[mid1 ...]      and nums2[mid2 ...]
            print(mid1, mid2)
            if Solution.check(nums1, mid1, nums2, mid2):
                print('break')
                break
            elif Solution.move_left_pointer(nums1, mid1, nums2, mid2): # move the left pointer
                print('left')
                left = mid1 + 1
            else:                          # move the right pointer
                print('right')
                right = mid1
        return Solution.get_median(nums1, mid1, nums2, mid2, left, right)

"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 or not nums2:
            nums = nums1 + nums2
            n = len(nums)
            if n % 2 == 1:
                return nums[n//2]
            else:
                return (nums[n//2] + nums[n//2-1])/2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        # step 1: deal with the special cases when nums1 and nums2 do not overlap
        if nums1[-1] <= nums2[0]:
            if total % 2 == 1:
                return nums2[n - half - 1]
            else:
                if m == n:
                    return (nums1[-1] + nums2[0]) / 2
                else:
                    return (nums2[n - half] + nums2[n - half - 1]) / 2
        if nums1[0] >= nums2[-1]:
            if total % 2 == 1:
                return nums2[half]
            else:
                if m == n:
                    return (nums1[0] + nums2[-1]) / 2
                else:
                    return (nums2[half - 1] + nums2[half]) / 2 

        # step 2: deal with the normal cases where nums1 and nums2 overlap
        low, high = 0, len(nums1)
        while low <= high:
            # print(low, high)
            mid1 = (low + high) // 2   # the left side is [0 ... mid1-1], right side is [mid1 ...]
            mid2 = half - mid1         # the left side is [0 ... mid2-1], right side is [mid2 ...]
            nums1_left  = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            nums1_right = nums1[mid1] if mid1 < m else float('inf')
            nums2_left  = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            nums2_right = nums2[mid2] if mid2 < n else float('inf')
            
            if nums1_right < nums2_left:
                low  = mid1 + 1
            elif nums1_left > nums2_right:
                high = mid1
            else:
                break

        if total % 2 == 1:
            return min(nums1[mid1] if mid1 < m else float('inf'), nums2[mid2] if mid2 < n else float('inf'))
        else:
            left_max = max(nums1[mid1-1] if mid1 > 0 else float('-inf'), nums2[mid2-1] if mid2 > 0 else float('-inf'))
            right_min = min(nums1[mid1] if mid1 < m else float('inf'), nums2[mid2] if mid2 < n else float('inf'))
            return (left_max + right_min) / 2


def test1():
    nums1 = [-2, 0, 2, 4]
    nums2 = [1, 3, 5, 7, 9]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test2():
    nums1 = [2]
    nums2 = [1,3]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))

def test3():
    nums1 = [6, 8, 10]
    nums2 = [-5, -3, -1, 1, 3, 5]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test4():
    nums1 = [1,2,2]
    nums2 = [1,2,3]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test5():
    nums1 = [1]
    nums2 = [1]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()


def test6():
    nums1 = [1,2,3,12]
    nums2 = [11,12,13,14]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test7():
    nums1 = [3,12,13]
    nums2 = [1,2,3,4]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test8():
    nums1 = [1]
    nums2 = [2, 3, 4]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test9():
    nums1 = [3]
    nums2 = [1, 2, 4]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test10():
    nums1 = [2]
    nums2 = [1,3,4,5]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()

def test11():
    nums1 = [2]
    nums2 = [1,3,4]
    print(nums1)
    print(nums2)
    s = Solution()
    print('median is', s.findMedianSortedArrays(nums1, nums2))
    print()




if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    # test6()
    # test7()
    # test8()
    # test9()
    # test10()
    test11()




''' testcase
[1,3]\n[2]

[-2, 0, 2, 4]\n[1, 3, 5, 7, 9]

'''

# @lc code=end

