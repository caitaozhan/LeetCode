#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.27%)
# Likes:    5262
# Dislikes: 639
# Total Accepted:    742.3K
# Total Submissions: 2.9M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#

import time
from typing import List

# @lc code=start
class Solution2:
    ''' O(n^2) solution with optimization finally passed...
    '''
    def check_index(self, indexes, i, j):
        '''return True if there is one indx in indexes that is not i nor j
        '''
        for indx in indexes:
            if indx != i and indx != j:
                return True
        return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict

        size = len(nums)
        if size <= 2:
            return []

        mydict = defaultdict(list)
        for i, num in enumerate(nums):
            mydict[num].append(i)
        sol    = set()
        set_ij = set()
        for i in range(size):
            for j in range(i+1, size):
                if (nums[i], nums[j]) in set_ij:
                    continue
                target = 0 - nums[i] - nums[j]
                if target in mydict:
                    indexes = mydict[target]
                    if self.check_index(indexes, i, j):
                        t = tuple(sorted([nums[i], nums[j], target]))
                        if t not in sol:
                            sol.add(t)
                            tt = tuple(sorted([nums[i], nums[j]]))
                            set_ij.add(tt)
        sol_list = [0 for _ in range(len(sol))]
        for i, t in enumerate(sol):
            sol_list[i] = list(t)
        return sol_list


class Solution:
    ''' still O(n^2), but a lot faster. It is the sorting and only keys of the defaultdict counter are left
        that makes it faster by reducing duplicates examined
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        import bisect
        ans = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        nums = sorted(counter)         # only keys are remained, no values
        for i, a in enumerate(nums):   # a < b < c, first fix a, then find b, then find c
            two_sum = 0 - a
            left = bisect.bisect_left(nums, two_sum - nums[-1], i + 1)   # the lower bound of b
            right = bisect.bisect_right(nums, two_sum // 2, left)        # the higher bound of b
            for b in nums[left:right]:
                c = two_sum - b
                if c in counter and c > b:
                    ans.append([a, b, c])     # three different elements
            if counter[a] >= 2:
                c = 0 - 2*a
                if c in counter and c != a:
                    ans.append([a, a, c])     # two different elements
                if counter[a] >= 3:
                    if a*3 == 0:
                        ans.append([a, a, a]) # one different elements
        return ans


def test2():
    nums = [1,1,-2]
    nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    s = Solution()
    sol = s.threeSum(nums)
    print(len(sol))

def test3():
    nums = [-1,0,1]
    s = Solution()
    sol = s.threeSum(nums)
    print(len(sol))


if __name__ == '__main__':
    # test()
    # test1()
    # test2()
    # test3()
    pass
# @lc code=end

