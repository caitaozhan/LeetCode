#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

import math
from itertools import accumulate



class Prime:
    '''TLE, O(n*1.5)
    '''
    def __init__(self):
        def is_prime(num):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return True
            return False

        upper = 5*10**6
        self.prime = [1] * (upper)
        self.prime[0] = 0
        self.prime[1] = 0
        for i in range(2, upper):
            if is_prime(i):
                self.prime[i] = 0
        self.ans = list(accumulate(self.prime))


class Prime:
    '''Sieve of Eratosthenes
    '''
    def __init__(self):
        upper = 5*10**6
        self.prime = [1] * (upper)
        self.prime[0] = 0
        self.prime[1] = 0
        for i in range(2, int(math.sqrt(upper)) + 1):
            if self.prime[i] == 1:
                for j in range(i**2, upper, i):
                    self.prime[j] = 0
        self.ans = list(accumulate(self.prime))

class Solution:
    '''using a precomputed table
    '''
    myprime = Prime()

    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        return Solution.myprime.ans[n-1]



class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        prime = [1] * n
        prime[0] = 0
        prime[1] = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if prime[i] == 1:
                for j in range(i**2, n, i):
                    prime[j] = 0
        return sum(prime)



n = 123456
s = Solution()
print(s.countPrimes(n))
# print(s.numSquares(n))

# @lc code=end

