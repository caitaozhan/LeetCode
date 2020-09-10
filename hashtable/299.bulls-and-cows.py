#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
from collections import Counter
class Solution:
    '''first pass for bull, second pass for cow
    '''
    def getHint(self, secret: str, guess: str) -> str:
        bull, cow = 0, 0
        counter = Counter(secret)
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
                counter[s] -= 1

        for s, g in zip(secret, guess):
            if s != g and counter[g] > 0:
                cow += 1
                counter[g] -= 1
        return f'{bull}A{cow}B'
        
        
# @lc code=end

