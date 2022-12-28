#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

from typing import List

# @lc code=start
class Solution:
    '''monotonic stack (non-increasing)
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
            

temperatures = [73,74,75,71,69,72,76,73]
s = Solution()
print(s.dailyTemperatures(temperatures))

        
# @lc code=end

