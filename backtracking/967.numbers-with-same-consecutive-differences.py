#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#

from typing import List

# @lc code=start
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(stack: list):
            if len(stack) == n:
                ans.append(''.join(map(str, stack)))
                return

            for digit in range(10):
                if len(stack) == 0:
                    if digit == 0:
                        continue
                    else:
                        backtrack(stack + [digit])
                else:
                    if digit - stack[-1] == k:
                        backtrack(stack + [digit])
                    if  k != 0 and digit - stack[-1] == -k:
                        backtrack(stack + [digit])
        
        ans = []
        backtrack(stack=[])
        ans = [int(s) for s in ans]
        return ans


n= 3
k = 7
s = Solution()
print(s.numsSameConsecDiff(n, k))
        
# @lc code=end

