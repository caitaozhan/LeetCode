'''

You are given an integer array matches where matches[i] = [winneri, loseri] indicates that 
the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


'''

from collections import Counter
from typing import List

class Solution:
    '''using dict and Counter()
    '''
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}
        for a_win, b_lost in matches:
            if a_win not in count:
                count[a_win] = Counter([1])  # 1 is for win
            else:
                count[a_win][1] += 1
            if b_lost not in count:
                count[b_lost] = Counter([0]) # 0 is for lost
            else:
                count[b_lost][0] += 1
        
        ans = [[], []]
        for key, counter in count.items():
            if counter[0] == 1:
                ans[1].append(key)
            if counter[0] == 0:
                ans[0].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans


class Solution:
    '''using dict and list
       list is faster than the above Counter
    '''
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = {}
        for a_win, b_lost in matches:
            if a_win not in count:
                count[a_win] = [0, 1]     # [lost, win]
            else:
                count[a_win][1] += 1
            if b_lost not in count:
                count[b_lost] = [1, 0] 
            else:
                count[b_lost][0] += 1
        
        ans = [[], []]
        for key, val in count.items():
            if val[0] == 1:
                ans[1].append(key)
            if val[0] == 0:
                ans[0].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans



matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
s = Solution()
print(s.findWinners(matches))
