#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

from typing import List

# @lc code=start
class Solution:
    '''binary search
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binary(other, upper):
            low, high = 0, upper
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == other:
                    return mid
                elif numbers[mid] < other:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

        for i in range(len(numbers)):
            other = target - numbers[i]
            if other <= numbers[i]:
                other_index = binary(other, i - 1)
                if other_index != -1:
                    return [other_index + 1, i + 1]


class Solution:
    '''an interesting two pointers solutions
       move left pointer or right pointer according to the sum of the [pointers]
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                return [i + 1, j + 1]
            elif summ < target:
                i += 1
            else:
                j -=1


numbers = [0,0,3,4]
target = 0
s = Solution()
print(s.twoSum(numbers, target))
        
# @lc code=end

