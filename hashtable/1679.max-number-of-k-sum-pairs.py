#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

from collections import Counter

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter()
        for num in nums:
            counter[num] += 1
        
        ans = 0
        visited = set()
        for num in counter.keys():
            if num in visited:
                continue
            visited.add(num)
            other = k - num
            if other in counter:
                visited.add(other)
                if other != num:
                    ans += min(counter[num], counter[other])
                else:
                    ans += counter[num] // 2
        return ans

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter()
        ans = 0
        for num in nums:
            other = k - num
            if counter[other] > 0:
                counter[other] -= 1
                ans += 1
            else:
                counter[num] += 1
        return ans

        
# @lc code=end

