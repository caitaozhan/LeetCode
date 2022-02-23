#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mydict = {chr(65 + i):(i+1) for i in range(26)}
        summ = 0
        for ch in columnTitle:
            summ *= 26
            summ += mydict[ch]
        return summ


class Solution:
    '''ord() is the opposite of chr'''
    def titleToNumber(self, columnTitle: str) -> int:
        summ = 0
        for ch in columnTitle:
            summ = summ * 26 + (ord(ch) - ord('A') + 1)
        return summ
        
# @lc code=end

