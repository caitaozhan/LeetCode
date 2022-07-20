#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    '''since the length of s is too long, let's tackle it by using binary searach
       n = len(s), m = len(words), c = max len of word in words
       O(c*m*log(n))
    '''
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:

        def binary_search(nums, target, left):
            '''return the index of the first num in nums that is larger than target
               if doesn't exist, return -1
            '''
            low = left
            high = len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid
                elif nums[mid] <= target:
                    low = mid + 1
            if low < len(nums) and nums[low] > target:
                return low
            else:
                return -1

        def match(mydict: dict, word: str):
            mydict_left = {}
            for key in mydict.keys():
                mydict_left[key] = 0
            s_i = -1
            for ch in word:
                if ch not in mydict:
                    return False
                indx_list = mydict[ch]
                left = mydict_left[ch]
                indx = binary_search(indx_list, s_i, left)
                if indx == -1:
                    return False
                mydict_left[ch] = indx
                s_i = indx_list[indx]
            return True

        mydict = defaultdict(list)
        for i, ch in enumerate(s):
            mydict[ch].append(i)

        ans = 0
        for word in words:
            if match(mydict, word):
                ans += 1
        return ans

s = "dsahjpjahajha"
words = ["haja"]
s = "qlhxagxdqh"
words = ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]
so = Solution()
print(so.numMatchingSubseq(s, words))

# @lc code=end

