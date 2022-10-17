#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        myset = set()
        for ch in sentence:
            myset.add(ch)
            if len(myset) == 26:
                return True
        return False

# @lc code=end

