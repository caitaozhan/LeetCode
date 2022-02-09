#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

from typing import List
from collections import defaultdict, Counter


class Solution1:
    '''not optimal'''
    def findPairs(self, nums: List[int], k: int) -> int:
        mydict = defaultdict(list)
        for i, num in enumerate(nums):
            mydict[num].append(i)

        myset = set()
        for i, num in enumerate(nums):
            for j in mydict[num + k]:
                if j > i:
                    myset.add((nums[i], nums[j]))  # (smaller one, bigger one)
                    break
            for j in mydict[num - k]:
                if j > i:
                    myset.add((nums[j], nums[i]))  # (smaller one, bigger one)
                    break
        return len(myset)


# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        mydict = Counter(nums)

        counter = 0
        for key, val in mydict.items():
            if k == 0:
                if val >= 2:
                    counter += 1
            else:  # k > 0
                if mydict[key + k] >= 1:  # don't need to consider [key - k], since a pair is symmetric
                    counter += 1
        return counter


# @lc code=end

