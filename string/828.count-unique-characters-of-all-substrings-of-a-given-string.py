#
# @lc app=leetcode id=828 lang=python3
#
# [828] Count Unique Characters of All Substrings of a Given String
#

from collections import defaultdict

# @lc code=start
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mydict = defaultdict(list)
        for char in [chr(65 + i) for i in range(26)]:
            mydict[char].append(-1)
        for i, char in enumerate(s):
            mydict[char].append(i)
        for char in [chr(65 + i) for i in range(26)]:
            mydict[char].append(len(s))
            mydict[char] = mydict[char][::-1]

        summ = 0
        for char in s:
            cur = mydict[char][-2]
            pre = mydict[char][-1]
            nxt = mydict[char][-3]
            left = cur - pre
            right = nxt - cur
            summ += left*right
            mydict[char].pop()
            
        return summ

# @lc code=end

