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

arr = [52,96,27,99,46,30,29,22,57,12,26,84,38,78,30,87,38,59,55,41,17,28,81,62,99,35,17,0,59,97,63,87,44,80,83,59,0,55,65,82,15,45,12,95,67,73,61,89,7,6,22,72,45,51,77,64,70,43,87,10,41,96,58,38,73,60,4,86,24,81,88,66,80,47,100,17,83,4,73,83,84,72,84,86,26,0,41,21,33,7,5,85,78,3,76,44,97,9,88,33,66,23,43,21,44,94,63,22,36,57,74,75,40,44,67,78,91,3,22,68,46,10,50,56,80,95,15,82,100,10,14,78,67,79,79,73,56,31,44,7,98,100,81,98,70,40,43,21,80,4,90,47,48,70,56,21,53,97,2,0,0,3,32,100,19,49,100,84,12,97,58,5,99,90,96,29,55,75,83,24,18,95,79,16,26,6,59,51,28,25,97,8,50,49,14,21,83,0,95,72,7,69,71,11,39,24,90,20,2,94,36,43,32,59,19,77,29,30,48,12,58,40,42,16,38,13,48,27,9,33,54,100,40,79,36,75,54,30,7,3,83,32,12,82,57,47,48,4,34,83,0,70,50,91,69,6,6,29,29,47,91,95,95,86,60,36,73,18,33,59,48,57,32,5,99,13,1,7,65,26,19,64,94,68,63,3,9,13,46,73,28,90,41,8,36,52,16,64,53,50,62,87,1,1,61,8,63,69,20,86,12,34,51,54,11,28,44,50,55,6,46,86,3,10,82,72,2,17,16,33,48,72,98,30,12,18,14,63,50,44,29,26,92,100,29,39,96,71,88,96,11,57,42,1,57,100,1,59,38,64,11,32,75,42,1,71,31,90,62,28,56,30,26,66,81,53,65,8,53,95,52,62,10,26,58,70,16,81,46,52,36,70,29,43,73,36,30,23,7,85,90,85,15,0,85,35,89,61,67,35,70,90,78,32,37,57,68,61,17,28,9,0,72,44,93,33,28,0,97,16,43,77,86,81,27,2,93,85,64,53,41,63,30,52,45,14,72,27,45,59,88,15,81,47,7,70,80,73,100,70,41,62,66,56,17,86,12,59,30,30,4,82,83,1,76,64,57,83,13,26,80,23,67,18,61,76,11,1,51,48,48,84,96,93,55,47,45,66,27,53,34,46,54,7,47,47,76,63,59,20,12,31,6,35,22,71,34,44,56,47,10,19,33,61,19,93,41,57,67,95,31,31,6,79,94,54,63,93,67,2,56,23,46,96,13,73,23,74,77,61,41,48,3,11,40,82,61,77,25,11,82,79,88,11,73,70,77,6,15,3,6,27,77,26,7,7,24,2,19,76,20,56,49,4,92,51,30,42,80,66,88,8,64,58,65,46,47,86,94,98,82,53,58,30,18,74,66,54,62,22,25,65,11,76,39,6,85,5,38,21,72,25,77,62,84,85,6,39,97,59,53,58,28,68,73,89,81,38,72,43,85,20,71,10,21,58,14,93,4,59,52,60,21,26,1,21,76,100,81,54,39,36,93,93,85,63,41,59,37,19,17,2,72,55,76,50,25,96,34,81,83,88,73,85,83,28,64,100,23,22,65,11,7,63,19,78,70,82,70,7,32,75,23,64,22,57,77,69,1,56,80,87,65,83,99,72,75,100,55,35,94,77,13,1,67,40,49,13,43,78,23,72,10,56,77,94,15,79,87,27,29,68,42,77,39,32,96,45,73,85,4,73,0,63,60,50,78,91,94,91,66,2,1,58,92,88,52,48,76,63,2,19,0,43,82,74,29,95,76,39,30,72,67,92,28,12,80,5,98,94,20,95,62,60,41,47,5,61,65,30,86,53,97,69,38,97,34,27,78,7,7,23,12,57,75,56,94,24,31,21,17,41,58,54,12,70,27,29,37,34,6,47,29,62,11,67,31,88,38,30,20,16,26,59,99,73,34,8,32,26,24,31,95,85,40,37,40,8,99,18,12,97,41,83,67,84,70,27,26,48,60,51,47,70,33,74,67,8,31,38,63,72,3,41,12,51,6,91,33,85,43,85,35,10,45,17,71,71,100,76,28,24,51,12,2,67,80,37,25,28,78,43,91,94,50,27,39,57,68,28,100,94,23,18,59,10,35,53,69,65,67,51,33,72,96,75,9,50,74,33,38,65,89,100,43,28,0,91,89,17,89,90,82,67,16,25,62,62,42,66,30,35,75,39,57,9,11,86,77,24,69,77,61,65,31,29,70,77,29,20,18,97,1,74,7,2,11,11,4,47,51,98,25,93,97,33,85,45,30,73,88,1,91,79,60,81,45,32,39,82,5,35,76,73,64,29,56,26,20,73,61,32,28,95,31,34,85,5,1,100,49,56,44,36,5,26,2,9,4,15,7,9,1,85,25,84,70,28,31,56,26,18,4,89,50,47,62,19,80,27,85,56,64,47,12,55,25,4,92,58,23,90,54,65,60,84,17,5,43,33,79,24,57,65,88,88,52,15,76,6,31,78,99,26,90,40,76,81,2,68,56,98,94,4,54,35,98,19,71,70,93,62,74,94,44,58,44,91,76,87,1,12,35,88,99,44,97,26,100,36,11,78,31,45,22,63,42,95,44,4,25,19,6,49,20,43,72,61,76,72,83,67,31,23,7,53,24,94,0,46,32,3,78,60,55,59,9,10,20,40,30,20,65,48,23,2,80,7,40,26,46,23,60,45,22,30,19,29,15,100,14,18,62,30,84,14,20,86,18,6,88,7,81,91,66,10,11,6,69,47,92,41,58,48,90,41,100,91,75,12,19,67,79,36,4,32,3,12,66,61,22,43,58,29,7,73,47,65,34,83,60,36,23,69,64,30,28,32,79,80,12,88,12,19,32,40,35,84,58,82,81,0,22,19,72,25,70,62,77,91,17,34,100,69,79,61,66,79,78,94,75,42,58,33,82,3,16,94,0,100,71,9,3,27,36,12,76,95,28,37,2,60,12,99,41,91,55,32,89,46,92,22,50,42,0,89,6,77,30,65,18,63,42,19,33,8,69,56,59,39,78,57,10,14,46,65,30,23,70,34,93,92,5,80,29,88,44,9,64,10,98,17,3,70,2,36,61,49,56,30,2,27,71,22,68,23,88,75,71,100,0,100,59,68,52,74,62,98,42,71,84,49,10,49,10,3,24,95,87,28,82,49,62,79,17,92,44,14,8,35,47,53,46,26,45,59,92,25,65,30,14,55,90,5,30,60,16,48,67,48,92,84,64,12,42,51,35,63,55,13,37,81,78,51,24,72,2,61,55,62,67,31,27,12,63,0,67,87,89,76,31,31,99,78,65,83,36,88,56,28,25,21,100,6,77,89,82,7,91,37,50,94,21,46,99,2,24,84,94,46,58,25,26,15,58,71,2,76,60,84,66,67,16,48,70,38,15,55,21,54,1,53,98,73,69,45,56,82,97,44,96,43,19,8,46,24,18,76,4,41,86,35,99,85,14,78,27,4,22,50,59,64,64,64,16,5,24,59,78,32,82,84,91,56,81,99,71,98,47,99,74,88,62,58,9,28,31,45,61,64,12,22,97,75,93,79,2,94,42,76,51,24,84,36,87,34,54,74,23,62,38,87,90,60,42,99,99,25,80,68,44,98,44,19,76,14,41,56,20,100,54,60,79,19,51,92,44,27,18,54,83,64,85,66,82,51,77,64,12,73,6,46,68,20,25,65,41,29,29,94,34,96,35,44,29,57,1,75,20,95,69,85,37,83,99,56,82,59,82,0,27,68,91,22,4,57,64,54,95,38,33,24,11,82,63,92,13,15,13,80,31,1,63,15,98,45,61,90,14,81,8,99,58,81,73,66,9,15,41,22,83,84,85,69,100,98,92,61,29,1,12,20,61,21,40,19,27,63,9,74,9,51,18,60,24,26,40,92,55,71,77,4,58,68,34,10,89,84,67,99,84,98,96,53,100,26,64,26,58,49,44,29,90,87,7,75,53,99,74,78,74,63,72,88,91,93,82,80,42,25,69,36,98,62,99,31,27,72,97,45,92,24,41,50,22,84,28,99,94,94,36,38,92,89,73,35,85,95,91,29,71,75,99,57,61,88,48,2,93,84,57,10,47,25,89,95,65,32,55,50,69,8,76,0,80,68,34,2,79,69,20,73,16,10,14,89,8,17,81,17,38,30,9,6,34,36,52,86,63,28,40,26,71,20,20,99,60,44,38,89,41,89,2,25,79,5,22,54,67,42,7,97,18,27,67,26,19,80,15,11,26,24,67,18,14,19,59,39,62,62,68,28,88,67,91,88,27,81,86,40,91,15,51,69,22,29,56,30,58,57,99,55,79,19,1,100,19,29,99,91,65,29,5,43,73,66,48,71,42,16,18,65,27,100,5,13,1,80,89,70,56,96,23,45,7,60,35,90,19,73,66,88,54,17,53,82,46,47,56,84,97,55,81,7,20,30,35,67,95,1,98,62,100,22,55,46,74,8,67,29,19,3,83,30,78,61,3,56,21,12,20,39,93,56,63,7,72,76,91,27,34,60,41,77,87,78,76,25,4,44,0,56,37,27,1,17,85,68,91,89,35,54,81,15,98,48,17,26,11,83,96,44,60,97,15,80,56,5,98,76,25,47,35,80,29,54,41,57,21,31,52,68,3,55,19,80,10,80,19,90,80,15,100,21,92,33,24,61,5,78,45,57,88,55,70,55,95,99,53,82,69,14,60,60,26,36,70,34,55,40,43,75,50,19,13,92,54,6,71,69,26,83,11,61,74,65,21,39,42,27,41,40,92,4,79,41,78,82,26,50,63,1,59,41,76,69,0,3,30,86,16,12,27,14,70,17,86,69,53,19,99,43,82,85,34,51,55,68,50,94,53,3,92,73,48,72,50,1,18,93,20,31,87,94,16,9,12,66,32,16,73,70,17,98,29,28,54,77,0,93,25,62,41,68,85,50,93,3,22,5,77,10,42,78,90,38,33,0,90,57,53,91,70,93,61,83,56,84,80,62,95,86,63,75,6,66,89,79,41,49,66,5,45,15,32,45,38,13,71,12,49,81,51,49,31,22,72,94,57,15,65,9,15,85,3,60,52,15,87,53,7,85,93,46,11,47,86,87,100,28,73,23,83,97,24,58,66,17,94,27,61,82,53,85,33,37,97,55,49,15,94,21,70,92,12,94,32,20,7,60,26,28,52,100,18,95,89,76,58,93,72,89,22,11,51,74,11,37,41,46,90,12,4,88,29,40,83,17,48,79,71,98,11,54,50,75,29,97,66,99,14,90,44,23,51,97,20,52,9,43,60,43,98,82,30,50,5,57,18,2,47,100,39,94,59,74,54,67,84,9,72,63,70,72,1,84,59,63,23,52,10,69,88,78,67,51,59,33,95,55,46,58,85,63,21,37,56,78,62,61,30,98,43,9,76,53,6,41,22,18,36,70,97,36,6,18,44,48,18,29,59,62,14,94,70,41,24,73,34,21,69,56,70,23,48,83,32,84,86,97,70,60,29,86,47,92,99,71,70,16,4,64,32,80,62,72,46,72,52,73,40,47,90,59,70,61,6,50,89,4,90,60,29,92,96,69,62,76,24,17,7,72,100,41,88,94,71,23,74,58,53,88,71,20,80,22,89,57,52,29,36,81,71,83,13,41,29,89,89,70,38,64,78,73,18,86,57,95,73,22,26,9,63,84,33,22,11,62,21,96,26,27,10,73,86,77,55,49,63,43,14,3,27,6,17,94,75,10,75,9,19,57,46,98,77,35,26,80,87,89,55,99,5,79,43,69,24,25,14,92,33,59,94,87,16,77,4,47,94,70,94,19,98,87,11,64,4,16,30,11,77,78,80,64,17,3,83,26,7,46,4,9,62,65,39,65,35,76,33,56,9,68,72,85,23,9,39,3,28,13,60,19,43,96,76,19,85,64,66,87,85,30,4,3,83,26,49,0,12,52,34,7,70,13,48,41,18,91,34,12,14,80,84,11,39,14,51,18,55,85,55,46,52,16,8,20,88,66,86,34,8,39,59,96,35,33,34,70,97,45,93,11,20,9,79,73,3,69,98,35,4,87,40,64,28,71,51,92,89,65,22,78,10,51,3,54,23,68,57,13,51,27,37,43,42,51,74,64,23,8,6,22,29,62,12,25,47,77,48,76,58,14,95,54,66,56,95,5,23,100,89,98,86,15,54,49,98,96,16,63,65,16,56,29,26,41,86,86,0,80,89,31,4,54,64,31,80,69,22,99,89,12,100,60,49,100,74,70,54,81,55,23,6,62,81,73,45,87,60,32,62,44,31,86,30,11,16,65,6,61,16,89,61,3,78,40,96,0,53,12,0,63,16,0,69,84,5,70,47,46,55,87,10,85,8,54,90,89,66,100,94,36,93,30,51,37,73,25,52,52,66,86,24,28,40,21,69,16,69,80,23,65,27,36,26,39,88,65,94,12,42,44,27,48,73,91,64,94,79,99,60,39,6,41,31,18,21,37,40,17,71,99,0,8,89,30,57,95,33,54,4,31,81,19,65,100,78,59,80,1,73,95,77,95,64,26,21,80,16,12,33,77,24,56,83,46,54,35,72,22,26,27,38,18,94,53,71,30,68,22,50,84,51,77,97,73,42,54,20,88,15,36,68,75,7,60,71,22,89,55,7,95,10,72,67,47,70,92,21,83,66,35,15,26,16,93,55,43,76,23,70,35,62,20,48,3,33,41,44,93,31,82,6,88,45,3,93,75,55,62,3,33,56,93,51,30,84,46,50,27,14,82,81,49,94,53,88,71,82,23,22,33,83,34,16,4,42,60,10,66]
target = 157

print(len(arr))

start = time.time()
s = Solution()
print(s.threeSumMulti(arr, target))
print('time', time.time() - start)