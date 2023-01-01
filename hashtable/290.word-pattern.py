#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    '''9/7/2020
    '''
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split(' ')
        if len(pattern) != len(str):    # WA for neglect this case
            return False
        
        mydic1 = {}  # pattern -> word
        mydic2 = {}  # word -> pattern
        for p, w in zip(pattern, str):
            if p not in mydic1:
                mydic1[p] = w
            else:
                if mydic1[p] != w:
                    return False
            if w not in mydic2:
                mydic2[w] = p
            else:
                if mydic2[w] != p:
                    return False
        return True


class Solution:
    '''redo on 1/1/2023
    '''
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()
        if len(pattern) != len(s_list):   # WA for neglect this case
            return False

        mydict = {}
        myset = set()
        for p, word in zip(pattern, s_list):
            if p in mydict:
                if mydict[p] != word:
                    return False
            else:
                if word in myset:  # prevent two p maps to a same word
                    return False
                mydict[p] = word
                myset.add(word)
        else:
            return True

# @lc code=end

