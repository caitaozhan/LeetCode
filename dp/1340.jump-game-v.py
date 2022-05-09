#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#

from typing import List

# @lc code=start
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr2 = [(num, index) for index, num in enumerate(arr)]
        arr2.sort()

        dp = [0] * len(arr)
        for _, i in arr2:
            maxx = 1
            # go left
            dstack = []
            left = max(-1, i - d - 1)
            for j in range(i, left, -1):
                if j != i and arr[j] >= arr[i]:
                    break
                maxx = max(dp[j] + 1, maxx)
            
            # go right
            right = min(len(arr), i + d + 1)
            for j in range(i, right):
                if j != i and arr[j] >= arr[i]:
                    break
                maxx = max(dp[j] + 1, maxx)
            
            dp[i] = maxx
        
        return max(dp)
            

# arr = [6,4,14,6,8,13,9,7,10,6,12]
# d = 2
# arr = [3,3,3,3,3]
# d = 3
arr = [83,11,83,70,75,45,96,11,80,75,67,83,6,51,71,64,64,42,70,23,11,24,95,65,1,54,31,50,18,16,11,86,2,48,37,34,65,67,4,17,33,70,16,73,57,96,30,26,56,1,16,74,82,77,82,62,32,90,94,33,58,23,23,65,70,12,85,27,38,100,93,49,96,96,77,37,69,71,62,34,4,14,25,37,70,3,67,88,20,30]
d = 29
# arr = [5, 6, 6, 7, 9, 5, 4, 10, 1, 5, 10]
# d = 5
s = Solution()
print(s.maxJumps(arr, d))


# from random import randint

# for _ in range(100):
#     arr = []
#     for _ in range(11):
#         arr.append(randint(1, 10))
#     print(arr)
#     print(5)


        
# @lc code=end

