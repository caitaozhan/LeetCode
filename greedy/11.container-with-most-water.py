#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    '''greedy
    '''
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] <= height[j]:         # move the smaller of [i] and [j]
                i += 1
                if height[i] <= height[i - 1]: # greedy
                    continue
            else:
                j -= 1
                if height[j] <= height[j + 1]:
                    continue
            ans = max(ans, (j - i) * min(height[i], height[j]))

        return ans

# @lc code=end

