#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (47.98%)
# Likes:    1887
# Dislikes: 83
# Total Accepted:    94.6K
# Total Submissions: 193.1K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#

# @lc code=start

from collections import Counter

class Solution2:
    '''this is constructing instead of reorganizing ...
    '''
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''
        counter = Counter(S)
        counter = [[ch, c] for ch, c in counter.items()]
        counter = sorted(counter, key=lambda x:x[1], reverse=True)
        if counter[0][1] > (len(S) + 1)/2:
            return ''
        s = ''
        i = 0
        while len(s) < len(S):
            i = 0
            while i < len(counter) and counter[i][0] == (s[-1] if s else ''):
                i += 1
            j = i
            while counter[i][1] > 0:
                s += counter[i][0]
                counter[i][1] -= 1
                j = (j+1)%len(counter)
                while j == i or counter[j][1] == 0:
                    j = (j + 1)%len(counter)
                    if len(s) == len(S):
                        return s
                s += counter[j][0]
                counter[j][1] -= 1
            counter = sorted(counter, key=lambda x:x[1], reverse=True)
            while counter and counter[-1][1] == 0:
                counter.pop()
        return s


class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = Counter(S)
        counter = counter.most_common()
        key, freq = counter[0]
        if freq > len(S) - freq + 1:
            return "" 
        arr = [key] * freq
        index = 0
        for key, freq in counter[1:]:
            for _ in range(freq):
                arr[index % len(arr)] += key
                index += 1
        return ''.join(arr)

def test():
    # S = 'aaaabbbccd'
    S = 'aab'
    # S = 'aaab'
    # S = 'a'
    # S = "zrhmhyevkojpsegvwolkpystdnkyhcjrdvqtyhucxdcwm"
    # S = "baaba"
    # S = "aabbcc"
    s = Solution()
    print(s.reorganizeString(S))

test()

# @lc code=end

