#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

'''

Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

 

Example 1:

Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

Note:

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''

from typing import List
from collections import Counter

# @lc code=start
class Solution2:
    '''basically problem 560 (subarray sum equals K) plus modulo %
    '''
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = [0]*len(A)
        prefix[0] = A[0]%K
        counter = Counter([prefix[0]])
        ans = 1 if prefix[0] == 0 else 0
        for i in range(1, len(A)):
            prefix[i] = (prefix[i-1] + A[i]) % K
            target = prefix[i] - 0
            ans += counter[target]
            if target == 0:
                ans += 1
            counter[prefix[i]] += 1
        return ans

class Solution3:
    '''Same idea constructing the prefix array and using modulo %, but a different way of counting
    '''
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = [0]*(len(A) + 1)
        for i in range(1, len(A) + 1):
            prefix[i] = (prefix[i-1] + A[i-1]) % K
        counter = Counter(prefix)
        return sum(v*(v-1)//2 for v in counter.values())

class Solution:
    '''just another way of writing. code is more neat
    '''
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = [0]
        for a in A:
            prefix.append((prefix[-1] + a) % K)
        counter = Counter(prefix)
        return sum(v*(v-1)//2 for v in counter.values())

# @lc code=end

