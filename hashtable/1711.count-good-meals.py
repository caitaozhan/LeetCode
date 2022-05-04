#
# @lc app=leetcode id=1711 lang=python3
#
# [1711] Count Good Meals
#

from collections import Counter

# @lc code=start
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter()
        for num in deliciousness:
            counter[num] += 1

        targets = [2**i for i in range(0, 22)]   # a mistake here at the range: range(0, 21)
        ans = 0
        for num in counter.keys():
            for two_sum in targets:
                other = two_sum - num
                if num <= other and counter[other] > 0:  # the trick here is the num <= other, it prevents duplicates
                    if num == other:
                        ans += counter[num] * (counter[num] - 1) // 2
                    else:
                        ans += counter[num] * counter[other]
        
        return ans % (10**9 + 7)


        
# @lc code=end

