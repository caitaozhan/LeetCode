#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            aval_set = set([chr(ord('a') + i) for i in range(26)])
            permutation = {}
            for p, w in zip(pattern, word):
                if p not in permutation:
                    if w in aval_set:         # preclude: multiple p --> w
                        permutation[p] = w
                        aval_set.remove(w)
                    else:
                        break
                else:
                    correct = permutation[p]
                    if w != correct:
                        break
            else:
                ans.append(word)
        return ans


        
# @lc code=end

