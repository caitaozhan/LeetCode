#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        mydict_max = defaultdict(int)
        mydict = defaultdict(list)
        for a, b in properties:
            mydict_max[a] = max(mydict_max[a], b)
            mydict[a].append([a, b])        
        ans = 0
        maxx = 0
        for key in sorted(mydict_max.keys(), reverse=True):
            for a, b in mydict[key]:
                if b < maxx:
                    ans += 1
            maxx = max(maxx, mydict_max[key])
        return ans

            
properties = [[1,5],[10,4],[4,3],[11,4],[10,3],[10,2],[11,3]]
s = Solution()
print(s.numberOfWeakCharacters(properties))

# @lc code=end

