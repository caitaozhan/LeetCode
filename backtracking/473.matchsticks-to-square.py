#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

from typing import List

# @lc code=start
class Solution:
    '''backtracking, O(4^N), need a trick to AC
    '''
    def __init__(self):
        self.ans = False

    def makesquare(self, matchsticks: List[int]) -> bool:

        def backtrack(i, sides, target):
            if self.ans:
                return
            if i == len(matchsticks):
                if sides[0] == sides[1] == sides[2] == sides[3] == target:
                    self.ans = True
                return
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]   # put the ith stick in the jth side
                    backtrack(i + 1, sides, target)
                    sides[j] -= matchsticks[i]
                    if sides[j] == 0:            # the trick! if [4,0,0] don't work, [0,4,0] also won't work
                        break

        matchsticks.sort(reverse=True)
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        side = total // 4
        sides = [0, 0, 0, 0]
        backtrack(0, sides, side)
        return self.ans



# matchsticks = [1,2,2,1,2]
matchsticks = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
matchsticks = [100,100,100,100,100,100,100,100,4,100,2,2,100,100,100]
print(len(matchsticks))
s = Solution()
print(s.makesquare(matchsticks))


# @lc code=end

