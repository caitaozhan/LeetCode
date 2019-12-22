#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (23.95%)
# Likes:    666
# Dislikes: 1047
# Total Accepted:    152.4K
# Total Submissions: 625.1K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

from typing import List
import copy
# import line_profiler

# @lc code=start
class Solution2:

    @staticmethod
    def get_words(s, indx, length, word_num):
        '''return a list of words, starting at indx'''
        words = []
        for i in range(word_num):
            start = indx + int(i * length)
            end   = indx + int((i+1) * length)
            words.append(s[start:end])
        return words


    @staticmethod
    def match_words(words, words_dict):
        '''
        Args:
            words      -- list<str>
            words_dict -- dict<str:int>
        '''
        words_dict = copy.deepcopy(words_dict)
        for word in words:
            count = words_dict.get(word)
            if count is None:
                return False
            words_dict[word] = count - 1
            if words_dict[word] < 0:
                return False
            # print(word)
        for word, count in words_dict.items():
            if count != 0:
                return False
        return True

    # @profile
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ''' s -- O(N)
            words -- O(M)
        '''
        from collections import defaultdict

        if len(words) == 0 or len(s) == 0:
            return []

        answer = []
        length = len(words[0])
        word_num = len(words)
        word_dict = defaultdict(int)
        for w in words:
            word_dict[w] += 1
        print(word_dict)
        for i in range(0, len(s) - int(length*word_num) + 1):
            words_tmp = Solution.get_words(s, i, length, word_num)
            if Solution.match_words(words_tmp, word_dict):
                answer.append(i)
        return answer


class Solution:

    @staticmethod
    def get_words(s_pro, indx, length, word_num):
        '''return a list of words, starting at indx'''
        words = []
        for i in range(word_num):
            start = indx + int(i * length)
            words.append(s_pro[start])
        return words


    @staticmethod
    def match_words(words, words_dict):
        '''
        Args:
            words      -- list<str>
            words_dict -- dict<str:int>
        '''
        words_dict = copy.deepcopy(words_dict)
        for word in words:
            count = words_dict.get(word)
            if count is None:
                return False
            words_dict[word] = count - 1
            if words_dict[word] < 0:
                return False
        for word, count in words_dict.items():
            if count != 0:
                return False
        return True

    @staticmethod
    def preprocess_s(s, length):
        s_pro = []
        for i in range(0, len(s)-length+1):
            s_pro.append(s[i:i+length])
        return s_pro

    # @profile
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ''' s -- O(N)
            words -- O(M)
        '''
        from collections import defaultdict

        if len(words) == 0 or len(s) == 0:
            return []

        answer = []
        length = len(words[0])
        s_pro = Solution.preprocess_s(s, length)
        word_num = len(words)
        word_dict = defaultdict(int)
        for w in words:
            word_dict[w] += 1
        for i in range(0, len(s) - int(length*word_num) + 1):
            words_tmp = Solution.get_words(s_pro, i, length, word_num)
            if Solution.match_words(words_tmp, word_dict):
                answer.append(i)
        return answer


def test1():
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    sol = Solution()
    print('input:', s, words)
    print('output:', sol.findSubstring(s, words))


def test2():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    sol = Solution()
    print('input:', s, words)
    print('output:', sol.findSubstring(s, words))

def test3():
    s = "b"
    words = ["foo"]
    sol = Solution()
    print('input:', s, words)
    print('output:', sol.findSubstring(s, words))

def test4():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","good"]
    sol = Solution()
    print('input:', s, words)
    print('output:', sol.findSubstring(s, words))

def test5():
    s = 'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab'
    words = ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"]
    sol = Solution()
    # print('input:', s, words)
    print('output:', sol.findSubstring(s, words))

if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()
# @lc code=end

