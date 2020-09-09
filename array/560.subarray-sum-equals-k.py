#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

from typing import List
from collections import Counter

# @lc code=start
class Solution:
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

