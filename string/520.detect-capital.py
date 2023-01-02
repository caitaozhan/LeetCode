#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        counter = 0
        for ch in word:
            if ch.isupper():
                counter += 1
        if counter == len(word) or counter == 0:
            return True
        if counter == 1 and word[0].isupper():
            return True
        return False


# @lc code=end
