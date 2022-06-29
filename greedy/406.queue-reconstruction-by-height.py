#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    '''O(n^2), insert one at a time
       sort by (ascending k, ascending height)
       with the same k value, put shorter people first
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (x[1], x[0]))
        indexdict = defaultdict(list)
        for i, item in enumerate(people):
            _, k = item
            indexdict[k].append(i)
        ans = []
        for key in sorted(indexdict.keys()):
            index = indexdict[key]
            min_j = -1
            for i in index:
                j = 0
                counter = 0
                height = people[i][0]
                while j < len(ans):
                    if ans[j][0] >= height:
                        counter += 1
                    j += 1
                    if j > min_j and counter == key:
                        min_j = j
                        break
                ans.insert(j, [height, key])
        return ans


class Solution:
    '''a more efficient O(n^2), insert one at a time
       sort by (decending height, ascending k)
       with the same height, put the smaller k value people first
       don't need to maintain a counter to figure out the correct location to insert, 
       instead directly use the k value as the index (doable becuase of dealing with taller people first, then shorter people)
    '''
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans


# people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
s = Solution()
print(s.reconstructQueue(people))

# @lc code=end

