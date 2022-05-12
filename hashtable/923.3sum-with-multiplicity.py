'''

Given an integer array arr, and an integer target, return the number of tuples i, j, k 
such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

'''

import time
import math
import bisect
from typing import List
from collections import defaultdict, Counter

class Solution:
    '''O(n^2) solution, reducing to a two-sum problem
    '''
    def solve_two_sum(self, arr, i, target):
        total = 0
        mydict = defaultdict(list)
        for j in range(i+1, len(arr)):
            tmp = target - arr[j]
            total += len(mydict[tmp])
            mydict[arr[j]].append(j)
        return total

    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        for i, num in enumerate(arr):
            two_sum = target - num
            ans += self.solve_two_sum(arr, i, two_sum)
        return ans % (10**9 + 7)



class Solution:
    '''O(n^2) solution, reducing to a two-sum problem
       using a counter and sort the keys, so it is more efficient
    '''
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        counter = Counter()
        for num in arr:
            counter[num] += 1
        arr = sorted(counter)   # prevent duplicate

        for i, a in enumerate(arr):
            two_sum = target - a
            
            right = bisect.bisect_right(arr, two_sum // 2, i+1)
            for b in arr[i+1:right]:  # a < b
                c = two_sum - b
                if c in counter and c != b and c != a:
                    ans += counter[a] * counter[b] * counter[c]  # a < b < c
                if c in counter and c == b:
                    ans += counter[a] * math.comb(counter[b], 2) # a < b = c
            
            if counter[a] >= 2:
                c = target - 2*a
                if c in counter and a < c:
                    ans += math.comb(counter[a], 2) * counter[c] # a = a < c
                if c == a:
                    ans += math.comb(counter[a], 3)              # a = a = a

        return ans % (10**9 + 7)



arr = [1,1,2,2,2,2]
target = 5

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8

print(len(arr))

start = time.time()
s = Solution()
print(s.threeSumMulti(arr, target))
print('time', time.time() - start)