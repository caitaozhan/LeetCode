#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

"""

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""

from typing import List
from collections import Counter

# @lc code=start
class Solution:
    '''the key here is to use a prefix array but not do it in one pass at the beginning,
       but do it together with a Counter() while constructing the prefix array.
    '''
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]*len(nums)
        prefix[0] = nums[0]
        counter = Counter([nums[0]])
        ans = counter[k]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
            target = prefix[i] - k
            ans += counter[target]
            if prefix[i] == k:
                ans += 1
            counter[prefix[i]] += 1
        return ans

def test():
    nums = [-1, -1, 1]
    k = 0
    s = Solution()
    print(s.subarraySum(nums, k))

test()

# @lc code=end

