#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (53.73%)
# Likes:    1466
# Dislikes: 66
# Total Accepted:    289.5K
# Total Submissions: 534K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    '''the key to solve this question is to discover the recursion tree
       doing iteration is a little bit hard here.
    '''
    def __init__(self):
        self.ans = []

    def dfs(self, comb, i, n, k):
        ''' i is the level of the recursion tree, starting from 1
        '''
        if i > k:
            return
        start = 1 if len(comb) == 0 else comb[-1]+1
        for node in range(start, n+1):
            if n - node < k - i:  # how many nodes left < the future depth of the recursion tree
                break
            comb.append(node)
            if len(comb) == k:
                self.ans.append(comb[:])
            self.dfs(comb, i+1, n, k)
            comb.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.dfs([], 1, n, k)
        return self.ans

def test():
    s = Solution()
    ans = s.combine(3, 6)
    print(len(ans), ans)

if __name__ == '__main__':
    test()

# @lc code=end

