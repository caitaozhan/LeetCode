#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

from typing import List

# @lc code=start
class Solution:
    '''using a decreasing stack, the tricky part is to iterate the nums from right to left
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        minarr = [float('inf')] * n   # minarr[i] is the minimum value from 0 ~ i
        minarr[0] = nums[0]
        for i in range(1, n):
            minarr[i] = min(minarr[i-1], nums[i])

        dstack = []
        for i in range(n-1, 0, -1):    # tricky: iterating from right to left, ignore [0]
            while dstack and nums[i] > nums[dstack[-1]]:  # nums[i] is the the 3 in 132, nums[dstack[-1]] is the 2 in 132
                if nums[dstack[-1]] > minarr[i-1]:        # minarr[i-1] is the 1 in 132, using the minimum is sufficient
                    return True
                dstack.pop()
            dstack.append(i)

        return False


nums = [-1,3,2,0]
nums = [3,5,0,3,4]
nums = [1,0,1,-4,-3]

s = Solution()
print(s.find132pattern(nums))

# @lc code=end

