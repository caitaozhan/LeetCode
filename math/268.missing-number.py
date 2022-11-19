#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

from typing import List

# @lc code=start
class Solution:
    '''O(nlogn) by using sorting
    '''
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


class Solution:
    '''O(n) time
       let the index equals the element, i.e., nums[i] == i
    '''
    def missingNumber(self, nums: List[int]) -> int:
        # step 1: see if elelment n is there
        n = len(nums)
        if max(nums) != n:
            return n
        nums.append(n) # n already exist, adding another n in the end doesn't affect

        # step 1: let nums[i] == i
        for i in range(n):
            cur = i
            if nums[cur] != cur:
                prev = nums[nums[cur]]
                nums[nums[cur]] = nums[cur]
                while nums[prev] != prev:
                    new_prev = nums[prev]
                    nums[prev] = prev
                    prev = new_prev

        # step 2: find the missing one
        for i in range(len(nums)):
            if i != nums[i]:
                return i


class Solution:
    '''using math...
    '''
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        real_sum = sum(nums)
        return expected_sum - real_sum




nums = [9,6,4,2,3,5,7,0,1]
# nums = [3, 0, 1]
s = Solution()
print(s.missingNumber(nums))


# @lc code=end

