#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (46.03%)
# Likes:    1846
# Dislikes: 86
# Total Accepted:    125.7K
# Total Submissions: 272.3K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#

'''
Solution2: do DFS. but time limit exceeded on [29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]\n35

Solution3: split the array into two half, do DFS on both sides, store all possible outcomes of each half. then consider all cases of the two half.
           this utilized that "The sum of elements in the given array will not exceed 1000"
Solution:  DP. an improvement of Solution2
'''

from typing import List

# @lc code=start

class Solution:
    '''DP: O(N x 1000)
    DP NOT in the traditional way, in terms of using the index
    dp[sum] = count, update this dp Counter
    '''
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        from collections import Counter
        dp = Counter()
        dp[nums[0]] = 1
        dp[-nums[0]] += 1  # test case [0,0,0,0,0,0,0,0,1]\n1

        for num in nums[1:]:
            new_dp   = Counter()
            for pre_sum, pre_count in dp.items():
                cur_sum = pre_sum + num
                new_dp[cur_sum] += pre_count
                cur_sum = pre_sum - num
                new_dp[cur_sum] += pre_count
            dp = new_dp
            # print(dp)
        if S in dp:
            return dp[S]
        else:
            return 0

class Solution3:
    ''' split the array into two half, do DFS on both sides, store all possible outcomes of each half. then consider all cases of the two half.
        this utilized that "The sum of elements in the given array will not exceed 1000"
    '''
    def __init__(self):
        from collections import Counter
        self.nums      = []
        self.counter1  = Counter()
        self.counter2  = Counter()
    
    def dfs(self, pre_sum, pre_indx, size, myset):
        cur_indx = pre_indx + 1
        if cur_indx == size:
            myset[pre_sum] += 1
            return
        cur_sum  = pre_sum + self.nums[cur_indx]  # +
        self.dfs(cur_sum, cur_indx, size, myset)
        cur_sum  = pre_sum - self.nums[cur_indx]  # -
        self.dfs(cur_sum, cur_indx, size, myset)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        counter = 0
        self.nums = nums
        if not self.nums:
            return 0

        size1 = int(len(self.nums)/2)
        self.dfs(0, -1, size1, self.counter1)
        self.dfs(0, size1 - 1, len(self.nums), self.counter2)

        for key_sum1, val_count1 in self.counter1.items():
            for key_sum2, val_count2 in self.counter2.items():
                if key_sum1 + key_sum2 == S:
                    counter += val_count1*val_count2
        return counter


class Solution2:
    '''do DFS
    '''
    def __init__(self):
        self.target    = 0
        self.counter   = 0
        self.nums      = []

    def dfs(self, previous_sum, pre_indx):
        '''the summation of previous elements in the array
        '''
        cur_indx = pre_indx + 1
        if cur_indx == len(self.nums):
            if previous_sum == self.target:
                self.counter += 1
            return
        cur_sum = previous_sum + self.nums[cur_indx]  # +
        self.dfs(cur_sum, cur_indx)
        cur_sum = previous_sum - self.nums[cur_indx]  # -
        self.dfs(cur_sum, cur_indx)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.target = S
        self.nums = nums
        self.dfs(0, -1)
        return self.counter

        
# @lc code=end

