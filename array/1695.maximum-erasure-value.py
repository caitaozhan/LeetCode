#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start

from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        prefix.append(0)
        mydict = {}
        j = -1
        ans = 0
        for i in range(n):
            if nums[i] not in mydict:
                mydict[nums[i]] = i
                a = prefix[i]
                b = prefix[j]
                ans = max(ans, a - b)
            else:
                a = prefix[i]
                j = max(j, mydict[nums[i]])
                b = prefix[j]
                mydict[nums[i]] = i
                ans = max(ans, a - b)
        return ans


nums = [4,2,4,5,6]
nums = [5,2,1,2,5,2,1,2,5]
s = Solution()
print(s.maximumUniqueSubarray(nums))

        
# @lc code=end

