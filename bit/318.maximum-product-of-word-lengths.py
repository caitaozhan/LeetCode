#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    '''using set
    '''
    def maxProduct(self, words: List[str]) -> int:
        mydict = {}
        for w in words:
            mydict[w] = set(w)

        ans = 0
        for i in range(len(words)):
            set_i = mydict[words[i]]
            for j in range(i + 1, len(words)):
                set_j = mydict[words[j]]
                for ch in set_i:
                    if ch in set_j:
                        break
                else:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans


class Solution:
    '''using the trick of bits -- bit mask, use 1 bit for a char
    '''
    def maxProduct(self, words: List[str]) -> int:
        char2number = {}
        for i in range(26):
            char = chr(ord('a') + i)
            char2number[char] = i

        bitmaskdict = {}
        for w in words:
            bitmask = 0
            for ch in w:
                bitmask |= (1 << char2number[ch])
            bitmaskdict[w] = bitmask
        
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitmaskdict[words[i]] & bitmaskdict[words[j]] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans

from collections import defaultdict

class Solution:
    '''using the trick of bits -- bit mask, use 1 bit for a char
       also reduce the looping over the words list
    '''
    def maxProduct(self, words: List[str]) -> int:
        char2number = {}
        for i in range(26):
            char = chr(ord('a') + i)
            char2number[char] = i

        bitmask2length = defaultdict(int)
        for w in words:
            bitmask = 0
            for ch in w:
                bitmask |= (1 << char2number[ch])
            bitmask2length[bitmask] = max(bitmask2length[bitmask], len(w))
        
        ans = 0
        keys = list(bitmask2length.keys())
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                if keys[i] & keys[j] == 0:
                    ans = max(ans, bitmask2length[keys[i]] * bitmask2length[keys[j]])

        return ans

# @lc code=end

