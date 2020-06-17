#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (34.36%)
# Likes:    4074
# Dislikes: 320
# Total Accepted:    463.2K
# Total Submissions: 1.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i][j] <= 10^5
# 
# 
#

# @lc code=start

from heapq import heappop, heappush
from typing import List

class Node:
    def __init__(self, indx, max_step):
        self.indx = indx
        self.max_step = max_step
        self.compare = - (self.indx + self.max_step)

    def __lt__(self, other):
        return self.compare < other.compare


class Solution2:
    '''greedy: uses a heap.
               not only sort the nodes by indx + max_step from large to small, 
               but also at each iteration, only consider the maximum indx + max_step
    '''
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        end_indx = len(nums) - 1
        start = Node(0, nums[0])
        heap = [start]
        while heap:
            cur_node = heappop(heap)
            cur_indx = cur_node.indx
            max_step = cur_node.max_step
            new_heap = []
            for i in range(1, max_step + 1):
                nxt_indx = cur_indx + i
                if nxt_indx == end_indx:
                    return True
                elif nxt_indx < end_indx and nums[nxt_indx] != 0:
                    heappush(new_heap, Node(nxt_indx, nums[nxt_indx]))
            heap = new_heap
        return False


class Solution3:
    '''greedy: do not use a heap, too much overhead
               every iteration, only pick the maximum nxt_indx + nums[nxt_indx]
    '''
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        end_indx = len(nums) - 1
        node = (0, nums[0])   # starting point
        maxx = nums[0]
        while node is not None:
            cur_indx = node[0]
            max_step = node[1]
            node = None
            for i in range(1, max_step + 1):
                nxt_indx = cur_indx + i
                if nxt_indx >= end_indx:
                    return True
                if nxt_indx + nums[nxt_indx] > maxx:
                    maxx = nxt_indx + nums[nxt_indx]
                    node = (nxt_indx, nums[nxt_indx])
        return False


class Solution:
    '''greedy: do not use a heap, too much overhead
               don't think in terms of iterations. interesting
    '''
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_i = nums[0]
        for i in range(1, len(nums)):
            if i <= max_i:
                max_i = max(max_i, i + nums[i])
            else:
                break
        return max_i >= len(nums) - 1


def test1():
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    #       *   *           *             *               * *           *     * *
    s = Solution()
    print(s.canJump(nums))

def test2():
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    #       *   *           *             *               * *           *     * *
    s = Solution2()
    print(s.canJump(nums))

if __name__ == '__main__':
    test1()
    test2()
    # pass
# @lc code=end

