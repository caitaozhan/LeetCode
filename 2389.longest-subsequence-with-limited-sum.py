'''

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that
you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements
without changing the order of the remaining elements.

'''

from typing import List
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixsum = list(accumulate(nums))
        ans = []
        for q in queries:
            idx = bisect_right(prefixsum, q)
            ans.append(idx)
        return ans
