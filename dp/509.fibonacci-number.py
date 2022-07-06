#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        arr = [0] * (n+1)
        arr[1] = 1
        for i in range(2, n+1):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[n]

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        a, b = 0, 1
        c = None
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c

        return c


from functools import lru_cache

class Solution:
    def fib(self, n: int) -> int:

        @lru_cache(None)
        def dp(n):
            if n == 0:
                return 0
            if n == 1:
                return 1

            return dp(n-1) + dp(n-2)
        
        return dp(n)

        

        
# @lc code=end

