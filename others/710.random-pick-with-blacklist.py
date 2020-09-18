#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#
# https://leetcode.com/problems/random-pick-with-blacklist/description/
#
# algorithms
# Hard (32.39%)
# Likes:    336
# Dislikes: 65
# Total Accepted:    13.8K
# Total Submissions: 42.5K
# Testcase Example:  '["Solution", "pick", "pick", "pick"]\n[[1, []], [], [], []]'
#
# Given a blacklist B containing unique integers from [0, N), write a function
# to return a uniform random integer from [0, N) which is NOT in B.
# 
# Optimize it such that it minimizes the call to system’s Math.random().
# 
# Note:
# 
# 
# 1 <= N <= 1000000000
# 0 <= B.length < min(100000, N)
# [0, N) does NOT include N. See interval notation.
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
# 
# 
# Example 3:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
# 
# 
# Example 4:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, N and the blacklist B. pick has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
#

from typing import List
from random import randint
from itertools import accumulate
from bisect import bisect_left

# @lc code=start
class SolutionTLE:
    '''TLE, because N is up to 1_000_000_000
    '''
    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.blacklist = set(blacklist)

    def pick(self) -> int:
        pick = randint(0, self.N-1)
        while pick in self.blacklist:        
            pick = randint(0, self.N-1)
        return pick


class Solution:
    '''first create all the "sub-whitelist", then pick two times. 
       first pick is to pick the sub-whitelist, then pick a number in the sub-whitelist
    '''
    def __init__(self, N: int, blacklist: List[int]):
        self.N = N
        self.blacklist = sorted(blacklist)
        self.blacklist.insert(0, -1)
        self.blacklist.append(self.N)
        self.sublist = []
        self.sublist_len = []
        self.init_sublist()

    def init_sublist(self):
        i = 0
        while i < len(self.blacklist) - 1:
            if self.blacklist[i] != self.blacklist[i+1]-1:
                self.sublist.append((self.blacklist[i]+1, self.blacklist[i+1]))
                self.sublist_len.append(self.blacklist[i+1] - self.blacklist[i])
            i += 1
        if not self.sublist:
            self.sublist.append((0, self.N))
            self.sublist_len.append(self.N)
        else:
            self.sublist_len = list(accumulate(self.sublist_len))

    def pick(self) -> int:
        pick_sublist = randint(1, self.sublist_len[-1])
        indx = bisect_left(self.sublist_len, pick_sublist)
        sublist = self.sublist[indx]
        return randint(sublist[0], sublist[1]-1)


def test():
    n = 12
    b = [0,1,5,6,8]
    s = Solution(n, b)
    for _ in range(10):
        print(s.pick())

test()
# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
# @lc code=end

