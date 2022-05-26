#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

from typing import List

# @lc code=start
class Solution:
    '''O(n^2) will TLE, tried to do some optimizations but failed
    '''
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = {}          # (w, h) -> size, pre_w, pre_h
        envelopes.sort()
        for w, h in envelopes:
            maxx = 0
            cur_pre_w = None
            cur_pre_h = None
            for key, val in dp.items():
                pre_w, pre_h = key
                size, _, _ = val
                if pre_w < w and pre_h < h:
                    if size > maxx:
                        maxx = size
                        cur_pre_w = pre_w
                        cur_pre_h = pre_h
            dp[(w, h)] = (maxx + 1, cur_pre_w, cur_pre_h)
        
        return max([val[0] for val in dp.values()])

from bisect import bisect_left

class Solution:
    '''clever O(nlogn) solution: sort, extract the second dimension, binary search
    '''
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        envelopes_h = [sec for _, sec in envelopes]  # extract the second dimension
        dp = []
        for h in envelopes_h:
            i = bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h

        return len(dp)



envelopes = [[5,4],[6,4],[6,7],[2,3],[8,8],[8,7],[6,1],[7,2]]
s = Solution()
print(s.maxEnvelopes(envelopes))


# @lc code=end

