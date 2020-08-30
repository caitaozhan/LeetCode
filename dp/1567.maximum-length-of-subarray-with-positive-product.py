"""

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.


Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].
Example 4:

Input: nums = [-1,2]
Output: 1
Example 5:

Input: nums = [1,2,3,5,-6,4,0,10]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

"""


from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp_pos = [0]*len(nums)
        dp_neg = [0]*len(nums)
        if nums[0] > 0:
            dp_pos[0], dp_neg[0] = 1, 0
        elif nums[0] < 0:
            dp_pos[0], dp_neg[0] = 0, 1
        else:
            dp_pos[0], dp_neg[0] = 0, 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp_pos[i], dp_neg[i] = 0, 0
            elif nums[i] > 0:
                if dp_pos[i-1] == 0 and dp_neg[i-1] == 0:
                    dp_pos[i], dp_neg[i] = 1, 0
                elif dp_pos[i-1] > 0 and dp_neg[i-1] == 0:
                    dp_pos[i] = dp_pos[i-1] + 1
                    dp_neg[i] = 0
                elif dp_pos[i-1] == 0 and dp_neg[i-1] > 0:
                    dp_pos[i] = 1
                    dp_neg[i] = dp_neg[i-1] + 1
                elif dp_pos[i-1] > 0 and dp_neg[i-1] > 0:
                    dp_pos[i] = dp_pos[i-1] + 1
                    dp_neg[i] = dp_neg[i-1] + 1
                else:
                    pass
            else: # nums[i] < 0
                if dp_pos[i-1] == 0 and dp_neg[i-1] == 0:
                    dp_pos[i], dp_neg[i] = 0, 1
                elif dp_pos[i-1] > 0 and dp_neg[i-1] == 0:
                    dp_pos[i] = 0
                    dp_neg[i] = dp_pos[i-1] + 1
                elif dp_pos[i-1] == 0 and dp_neg[i-1] > 0:
                    dp_pos[i] = dp_neg[i-1] + 1
                    dp_neg[i] = 1
                elif dp_pos[i-1] > 0 and dp_neg[i-1] > 0:
                    dp_pos[i] = dp_neg[i-1] + 1
                    dp_neg[i] = dp_pos[i-1] + 1
                else:
                    pass
        return max(dp_pos)