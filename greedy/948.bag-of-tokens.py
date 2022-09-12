#
# @lc app=leetcode id=948 lang=python3
#
# [948] Bag of Tokens
#

from typing import List

# @lc code=start
class Solution:
    '''greedy:
        1) if you want to play the token face up, pick the token with small power
        2) if you want to play the token face down, pick the token with large power
        --> sort the tokens, low pointer + high pointer
    '''
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        tokens.sort()             # greedy
        score = 0
        n = len(tokens)
        i, j = 0, n - 1
        while i <= j:
            if power >= tokens[i]:
                score += 1
                ans = max(ans, score)
                power -= tokens[i]
                i += 1
            else:
                if score >= 1:
                    score -= 1    # to keep the game going
                    power += tokens[j]
                    j -= 1
                else:
                    break         # game cannot play any more
        return ans


        
# @lc code=end

