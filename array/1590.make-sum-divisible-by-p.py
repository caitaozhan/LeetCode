'''

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109

'''

from typing import List
from itertools import accumulate

class SolutionTLE:
    '''O(n^2) solution, TLE
    '''
    def minSubarray(self, nums: List[int], p: int) -> int:
        acc = list(accumulate(nums))
        summ = acc[-1]
        if summ % p == 0:
            return 0
        for i in range(1, len(nums)):        # length of the subarray
            for j in range(i-1, len(nums)):
                right = acc[j]
                left = acc[j-i] if j-i >= 0 else 0
                sub_sum = right - left
                if (summ - sub_sum)%p == 0:
                    return i
        return -1


class Solution2:
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        target = summ % p
        if target == 0:
            return 0

        prefix = [0]*len(nums)
        prefix[0] = nums[0] % p
        latest = {prefix[0]:0}
        ans = float('inf')
        for i in range(1, len(nums)):
            prefix[i] = (prefix[i-1] + nums[i]) % p
            x = (prefix[i] - target) % p
            if x in latest:
                ans = min(ans, i - latest[x])
            if x == 0:
                ans = min(ans, i + 1)
            latest[prefix[i]] = i
        return ans if ans != float('inf') and ans != len(nums) else -1


class Solution:
    '''almost same as Solution2, just different way of handling the edge case
       where the current (right) pointer is at i and we want to find the left pointer j is at -1
    '''
    def minSubarray(self, nums: List[int], p: int) -> int:
        summ = sum(nums)
        target = summ % p
        if target == 0:
            return 0

        prefix = [0]*len(nums)
        prefix[0] = nums[0] % p
        latest = {0:-1}
        latest[prefix[0]] = 0
        ans = float('inf')
        for i in range(1, len(nums)):
            prefix[i] = (prefix[i-1] + nums[i]) % p
            x = (prefix[i] - target) % p
            if x in latest:
                ans = min(ans, i - latest[x])
            latest[prefix[i]] = i
        return ans if ans != float('inf') and ans != len(nums) else -1

nums = [8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
p = 148
# nums= [1,2,3]
# p = 7

# s = SolutionTLE()
s = Solution()
print(s.minSubarray(nums, p))
