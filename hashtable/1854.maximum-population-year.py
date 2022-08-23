#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#

from typing import List
from typing import Counter

# @lc code=start
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population = Counter()
        for birth, death in logs:
             for i in range(birth, death):
                population[i] += 1
        maxx = max(population.values())
        for year, count in sorted(population.items()):
            if count == maxx:
                return year
        
# @lc code=end

