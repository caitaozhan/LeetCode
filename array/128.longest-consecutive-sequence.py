#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

from typing import List

# @lc code=start
class Solution:
    '''a top down DP approach in O(n)
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        def dfs(num):
            '''return:
                the recursion depth of num
            '''
            if num not in mydict:    # num does not exist, so return 0
                return 0
            else:
                if mydict[num] is not None:
                    return mydict[num]
                else:
                    rtn = dfs(num-1)
                    mydict[num] = rtn + 1
                    return mydict[num]

        if not nums:
            return 0

        mydict = {}
        for num in nums:
            mydict[num] = None   # unvisited
        
        for num in nums:
            if mydict[num] is None:
                dfs(num)
        
        return max(list(mydict.values()))


from functools import lru_cache

class Solution:
    '''a top down DP approach in O(n)
       use a decorator called lru_cache that makes the code more simple
    '''
    def longestConsecutive(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dp(num):
            '''return:
                the recursion depth of num
            '''
            if num not in myset:    # num does not exist, so return 0
                return 0
            else:
                return dp(num-1) + 1

        ans = 0
        myset = set(nums)
        
        for num in nums:
            ans = max(ans, dp(num))
        
        return ans

nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))

        
# @lc code=end

