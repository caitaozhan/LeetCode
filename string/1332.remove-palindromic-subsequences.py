#
# @lc app=leetcode id=1332 lang=python3
#
# [1332] Remove Palindromic Subsequences
#

# @lc code=start
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        def ispalindrome(s):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True    
            
        
        if ispalindrome(s):
            return 1
        
        return 2
        
# @lc code=end

