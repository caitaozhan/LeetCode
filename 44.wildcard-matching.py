#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (23.69%)
# Likes:    1605
# Dislikes: 93
# Total Accepted:    221.8K
# Total Submissions: 921.7K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false
# 
# 
#

import time


'''
"aa"\n"a"\n"aa"\n"*"\n"cb"\n"?a"\n"adceb"\n"*a*b"\n"acdcb"\n"a*c?b"\n"abcdcc"\n"a*c"\n"aaaa"\n"***a"\n"aaba"\n"*a**b*"\n"aa"\n"*"\n"aab"\n"c*a*b"

"aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba"\n"*****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*"

"babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"\n"b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"

"abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"\n"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"

"mississip"\n"m??*ss*?i*"

"aabc"\n"**abc"
'''

# @lc code=start
class Solution:
    '''Recursive solution -- with memorization
    '''
    def __init__(self):
        self.memorize = []  # memorize the smaller substrings s[i:] and p[j:] that doesn't match

    def update_memorize(self, s, i, p, j):
        s_no_match_new = len(s) - i  # the last s_no_match charecters of s
        p_no_match_new = len(p) - j  # the last p_no_match charecters of p
        new_memorize = []
        keep_new = True
        for s_no_match_old, p_no_match_old in self.memorize:
            if s_no_match_old < s_no_match_new or p_no_match_old < p_no_match_new:
                new_memorize.append((s_no_match_old, p_no_match_old))
            if s_no_match_old < s_no_match_new and p_no_match_old < p_no_match_new:
                keep_new = False
        if keep_new:
            new_memorize.append((s_no_match_new, p_no_match_new))
        self.memorize = new_memorize

    def check_memorize(self, s, i, p, j):
        prune = False
        s_sub_len = len(s) - i
        p_sub_len = len(p) - j
        for s_no_match, p_no_match in self.memorize:
            if s_sub_len >= s_no_match and p_sub_len >= p_no_match:
                prune = True  # when two smaller substrings of s[i:] and p[j:] don't match, s[i:] and p[j:] is guaranteed not to match, so prune it
                break         # the  two smaller substrings here are the last s_no_match charecters of s and the last p_no_match charecters of p
        return prune

    def isMatch_helper(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:  # both match to the end
            return True
        if len(s) == 0 or len(p) == 0:   # one comes to the end but the other not
            return False
        if s[0] == p[0] or p[0] == '?':  # match
            return self.isMatch_helper(s[1:], p[1:])
        if s[0] != p[0] and p[0] == '*':
            i, j = 0, 0
            while j < len(p):            # j points to the first char that is not '*'
                if p[j] != '*':
                    break
                j += 1
            counter = 0
            for k in range(j+1, len(p)): # for pruning the search space for i
                if p[k] != '*':
                    counter += 1
            while i < len(s)-counter and j < len(p):
                if s[i] == p[j] or (s[i] != p[j] and p[j] == '?'):
                    if self.check_memorize(s, i, p, j):
                        return False
                    if self.isMatch_helper(s[i:], p[j:]):
                        return True
                    else:
                        self.update_memorize(s, i, p, j)
                i += 1
        return False                     # case for s[0] != p[0] and p[0] is not a wildcard:

    def isMatch(self, s: str, p: str) -> bool:
        s = s + '1'
        p = p + '1'  # so that the last charecter is not '*'. Of course there are other ways to deal with it
        return self.isMatch_helper(s, p)


class Solution3:
    '''Finite state machine (FSM) solution. elegant
       https://leetcode.com/problems/wildcard-matching/discuss/138878/Finite-state-machine-with-Python-and-dictionary.-13-lines-O(p%2Bs)-time
    '''
    def isMatch(self, s: str, p: str) -> bool:
        # step 1: build a FSM: 1) state 2) transition
        state = 0
        transition = {}
        for char in p:
            if char != '*':
                transition[(state, char)] = state + 1
                state += 1
            else:
                transition[(state, char)] = state
        final_state = state
        # step 2: start running the FSM
        states = set([0])
        for char in s:
            new_states = set()
            for state in states:
                for token in [char, '*', '?']:
                    next_state = transition.get((state, token))
                    if next_state is not None:
                        new_states.add(next_state)
            states = new_states
        return final_state in states


class Solution2:
    '''DP solution, nice solution. First I defined the subproblem so that dp[i][j] are {0, 1, 2, 3...}, this way is somewhat hard, so failed
       The right way of defining the subproblem is that dp[i][j] is {True,False}
    '''
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 1
        j = 1
        while j-1 < len(p):
            if p[j-1] != '*':
                break
            dp[0][j] = 1
            j += 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == p[j-1] or p[j-1] == '?':
                    if dp[i-1][j-1]:              #  precise match
                        dp[i][j] = 1
                if s[i-1] != p[j-1] and p[j-1] == '*':
                    if dp[i][j-1] or dp[i-1][j]:  # '*' either {skip} or {matching more charecters}
                        dp[i][j] = 1
        return dp[m][n]

# @lc code=end

def test():
    s = "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
    p = "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"
    # s = "mississip"
    # p = "m??*ss*?i*"
    sol = Solution()
    start = time.time()
    ans = sol.isMatch(s, p)
    end = time.time()
    print(ans, end-start)

if __name__ == '__main__':
    pass
    # test()
