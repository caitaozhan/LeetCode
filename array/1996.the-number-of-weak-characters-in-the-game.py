#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    '''use a dictionary, the space complexity is high: O(n)
       time complexity: O(nlogn)
    '''
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


class Solution:
    '''a smarter sorting, the time complexity is also O(nlogn) but in practice slower than the above Solution
       but the space complexity is lower: O(logn)
    '''
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        n = len(properties)
        maxx = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            if properties[i][1] < maxx:
                ans += 1
            else:
                maxx = properties[i][1]
        return ans


            
properties = [[1,5],[10,4],[4,3],[11,4],[10,3],[10,2],[11,3]]
s = Solution()
print(s.numberOfWeakCharacters(properties))

# @lc code=end

