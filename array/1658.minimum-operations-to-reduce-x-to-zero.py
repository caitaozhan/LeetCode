#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

from typing import List

# @lc code=start
class Solution:
    '''O(nlogn) solution using binary search
    '''
    def binary_search(self, suffix, upper, target):
        low, high = 0, upper
        while low <= high:
            mid = (low + high) // 2
            if suffix[mid] == target:
                return mid
            elif suffix[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        prefix.insert(0, 0)
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
        suffix.append(0)
        suffix.reverse()

        ans = float('inf')
        for i in range(n):
            target = x - prefix[i]
            j = self.binary_search(suffix, n-i, target)
            if j != -1:
                ans = min(ans, i + j)
        
        ans = -1 if ans == float('inf') else ans
        return ans

class Solution:
    '''O(n) solution using dictionary
    '''
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        prefix.insert(0, 0)
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
        suffix.append(0)
        suffix.reverse()
        suffixdict = {}
        for i, num in enumerate(suffix):
            suffixdict[num] = i

        ans = float('inf')
        for i in range(n):
            target = x - prefix[i]
            if target in suffixdict:
                j = suffixdict[target]
                if i + j <= n:
                    ans = min(ans, i + j)
        
        ans = -1 if ans == float('inf') else ans
        return ans
        
nums = [3,1,1,2,4]
x = 5

nums = [3,2,20,1,1,3]
x = 10

nums = [1,1]
x = 3

s = Solution()
print(s.minOperations(nums, x))



# @lc code=end

