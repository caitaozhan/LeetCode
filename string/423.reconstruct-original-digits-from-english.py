#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#

'''
zero - z
two - w
four - u
six - x

five - u,f
seven - x,s

three - zu,r

one - zwu,o
eight - zur,h

nine - xfh,i
'''

from collections import Counter

# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        sol = ""
        digitmap = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
        order = [['z','zero'], ['w','two'], ['u','four'], ['x','six'], ['f','five'], ['s', 'seven'], ['r', 'three'], ['o', 'one'], ['h', 'eight'], ['i', 'nine']]
        for ch, word in order:
            if count[ch] != 0:
                repeat = count[ch]
                sol += digitmap[word] * repeat
                for ch2 in word:
                    count[ch2] -= repeat

        sol = ''.join(sorted(sol))
        return sol
# @lc code=end

