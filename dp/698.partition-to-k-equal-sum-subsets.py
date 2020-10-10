#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (44.86%)
# Likes:    2210
# Dislikes: 131
# Total Accepted:    97.5K
# Total Submissions: 216.7K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
# 
# 
#

from typing import List

# @lc code=start
class SolutionTLE:
    '''top down DP -- dfs with pruning and memoization
    '''
    def __init__(self):
        self.memo = {}
        self.nums = None

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        if summ % k != 0:
            return False
        self.nums = nums
        subsetsum = summ // k
        node = (len(nums)-1,) + (subsetsum,) * (k-1)
        ret = self.dfs(node)
        print(len(self.memo))
        return ret


    def dfs(self, node):
        '''
        Args:
            node -- tuple -- (i, subsetsum_1, ..., subsetsum_{k-1})
                             definition: if nums[1, ..., i] can be divided into subsets whose sum are
                             subsetsum_1, ..., subsetsum_{k-1}, then the node maps to value 1, otherwise map to value 0
        '''
        if node in self.memo:
            # print(node, self.memo[node])
            return self.memo[node]
        if not self.check_possible_i(node):
            return False
        if self.check_success(node):
            return True
        if not self.check_non_negative(node):
            return False

        i = node[0]
        node_tmp = list(node)
        node_tmp[0] = node_tmp[0] - 1
        ret = self.dfs(tuple(node_tmp))
        if ret is True:
            self.memo[tuple(node_tmp)] = True
            self.memo[node] = True
            return True
        else:
            self.memo[tuple(node_tmp)] = False

        for j in range(1, len(node)):
            node_tmp = list(node)
            node_tmp[0] = node_tmp[0] - 1
            node_tmp[j] = node_tmp[j] - self.nums[i]
            ret = self.dfs(tuple(node_tmp))
            if ret is True:
                self.memo[tuple(node_tmp)] = True
                self.memo[node] = True   # it is True if one of them is True
                return True
            else:
                self.memo[tuple(node_tmp)] = False
        self.memo[node] = False
        return False

    def check_possible_i(self, node):
        '''node[0] >= non-zero subset sums
        '''
        zero = node[1:].count(0)
        non_zero = len(node) - 1 - zero
        if node[0] < non_zero:
            return False
        return True

    def check_success(self, node):
        '''if all subsetsum goes down to 0, then it is a success
        '''
        for sssum in node[1:]:
            if sssum != 0:
                return False
        return True
    
    def check_non_negative(self, node):
        '''a node is valid if there is no negative values
        '''
        for e in node:
            if e < 0:
                return False
        return True


class Solution2():
    '''backtracking -- constructing the subsets
    '''
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: 
            return False

        def dfs(groups):
            if not nums: 
                return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if dfs(groups): 
                        return True
                    groups[i] -= v
                if not group:    # let the zeros be at the end of groups
                    break        # i.e. if the first element fails to put at the first group, then don't need to try putting it at the second group
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: 
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return dfs([0] * k)


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target:
            return False
        dp = [0] * (1 << len(nums))
        dp[0] = 1
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if dp[state] == 0:
                continue
            for i, num in enumerate(nums):
                nxt = state | (1 << i)
                if state != nxt and dp[nxt] == 0:
                    if num <= target - (total[state] % target):
                        dp[nxt] = 1
                        total[nxt] = total[state] + num
                    else:
                        break
        return True if dp[-1] == 1 else False


def test():
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    s = Solution()
    print(s.canPartitionKSubsets(nums, k))
test()

def test2():
    nums = [4,5,3,2,5,5,5,1,5,5,5,5,5,5,5,5]
    # print(len(nums))
    k = 14
    s = Solution()
    print(s.canPartitionKSubsets(nums, k))
# test2()

def test3():
    nums = [3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269]
    k = 5
    s = Solution()
    print(s.canPartitionKSubsets(nums, k))
# test3()

def test4():
    nums = [7628, 3147, 7137, 2578, 7742, 2746, 4264, 7704, 9532, 9679, 8963, 3223, 2133, 7792, 5911, 3979]
    k = 6
    s = Solution()
    print(s.canPartitionKSubsets(nums, k))
# test4()

# @lc code=end

