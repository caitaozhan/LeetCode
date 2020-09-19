'''

We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

Return the maximum total sum of all requests among all permutations of nums.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
Total sum: 11 + 8 = 19, which is the best that you can do.
Example 2:

Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
Example 3:

Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
Output: 47
Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
 

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i] <= 105
1 <= requests.length <= 105
requests[i].length == 2
0 <= starti <= endi < n

'''


import time
from typing import List
from collections import Counter
from itertools import accumulate
import numpy as np


class Solution:
    '''a small trick that can reduce the bottle neck in looping over the requests
    '''
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        counter = [0]*(len(nums)+1)
        for l, r in requests:
            counter[l] += 1      # smart trick
            counter[r+1] -= 1
        counter = list(accumulate(counter))[:len(nums)]
        counter.sort()
        nums.sort()
        return sum([counter[i]*nums[i] for i in range(len(nums))]) % MOD


class Solution2:
    '''TLE
    '''
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        indx_counter = Counter(range(len(nums)))
        start = time.time()
        for ran in requests:
            indx_counter += Counter(range(ran[0], ran[1]+1))
        print(time.time() - start)
        indx_sorted = indx_counter.most_common()
        nums = sorted(nums, reverse=True)
        new_nums = [0 for _ in range(len(nums))]
        for indx, num in zip(indx_sorted, nums):
            i = indx[0]
            new_nums[i] = num
        ans = 0
        acc = list(accumulate(new_nums))
        for ran in requests:
            right = acc[ran[1]]
            left = acc[ran[0]-1] if ran[0] > 0 else 0
            ans += right - left
        return ans


class Solution3:
    '''TLE
    '''
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        counter = [[i, 0] for i in range(len(nums))]
        start = time.time()
        for ran in requests:
            for i in range(ran[0], ran[1]+1):
                counter[i][1] += 1
        print(time.time() - start)
        indx_sorted = sorted(counter, key=lambda x:x[1], reverse=True)
        nums = sorted(nums, reverse=True)
        new_nums = [0 for _ in range(len(nums))]
        for indx, num in zip(indx_sorted, nums):
            i = indx[0]
            new_nums[i] = num
        ans = 0
        acc = list(accumulate(new_nums))
        for ran in requests:
            right = acc[ran[1]]
            left = acc[ran[0]-1] if ran[0] > 0 else 0
            ans += right - left
        return ans


class Solution4:
    '''accepted. but using numpy in LeetCode is like cheating
    '''
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        start = time.time()
        count = np.array([0]*len(nums))
        for req in requests:
            count[req[0]:req[1]+1] += 1
        print(time.time() - start)
        nums.sort()
        count.sort()
        ans = 0
        for n, c in zip(nums, count):
            ans = (ans + n * c) % MOD
        return ans



# nums = [1,2,3,4,5]
# requests = [[1,3],[0,1]]

# s = Solution3()
# print(s.maxSumRangeQuery(nums, requests))

# s = Solution2()
# print(s.maxSumRangeQuery(nums, requests))

# s = Solution()
# print(s.maxSumRangeQuery(nums, requests))

'''
[1,2,3,4,5]
[[1,3],[0,1]]
[1,2,3,4,5,6]
[[0,1]]
[1,2,3,4,5,10]
[[0,2],[1,3],[1,1]]
'''
