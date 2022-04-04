#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        # find the first unmatched
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                break
        if i >= j:
            return True
        
        # delete the left hand side [i]
        l = i + 1    # left
        r = j        # right
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l >= r:
            return True

        # delete the right hand side [j]
        l = i        # left
        r = j - 1    # right
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                break
        if l >= r:
            return True

        return False
        
# @lc code=end

