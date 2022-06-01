#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
class Solution:
    '''O(nk)
    '''
    def hasAllCodes(self, s: str, k: int) -> bool:
        myset = set()
        for i in range(len(s) - k + 1):
            substr = s[i:i+k]
            myset.add(substr)
        return len(myset) == 2**k


class Solution:
    '''O(n) by using rolling hash, convert binay to decimal
    '''
    def hasAllCodes(self, s: str, k: int) -> bool:
        arr = [False] * (1<<k)
        all_one = (1<<k) - 1
        hash_val = int(s[:k], 2)
        arr[hash_val] = True
        for i in range(k, len(s)):
            hash_val = ((hash_val << 1) & all_one) | int(s[i])
            arr[hash_val] = True
        return not(False in arr)


        
# @lc code=end

