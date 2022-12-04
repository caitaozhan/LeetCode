#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#

from heapq import heappush, heappop


class Racecar:
    '''precompute
    '''
    def __init__(self):
        def dp_helper(p: int, s: int) -> int:
            if (p, s) in dp:
                return dp[(p, s)]
            else:
                return float('inf')

        upper = 2 * 10 ** 4
        myset = set([i for i in range(1, 10001)])
        self.ans = [float('inf')] * 10001
        dp = {}
        heap = [(0, 0, 1)]     # (length of sequence, position, speed)
        while heap:
            length, p, s = heappop(heap)
            if p in myset:
                self.ans[p] = length
                myset.remove(p)
            if len(myset) == 0:
                return

            # instruction 'A'
            new_p = p + s
            new_s = s * 2
            new_length = length + 1
            if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                dp[(new_p, new_s)] = new_length
                heappush(heap, (new_length, new_p, new_s))

            # instruction 'R', either 'RA' or 'RRA', no point of 'RRRA'
            if s > 0:
                # 'RA'
                new_p = p - 1
                new_s = -2
                new_length = length + 2
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))
                # 'RRA'
                new_p = p + 1
                new_s = 2
                new_length = length + 3
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))
            if s < 0:
                # 'RA'
                new_p = p + 1
                new_s = 2
                new_length = length + 2
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))
                # 'RRA'
                new_p = p - 1
                new_s = -2
                new_length = length + 3
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))

class Solution:
    race_car = Racecar()

    def racecar(self, target: int) -> int:
        return Solution.race_car.ans[target]



class Solution:
    def racecar(self, target: int) -> int:
        def dp_helper(p: int, s: int) -> int:
            if (p, s) in dp:
                return dp[(p, s)]
            else:
                return float('inf')
    
        upper = 2 * 10 ** 4
        dp = {}
        heap = [(0, 0, 1)]     # (length of sequence, position, speed)
        while heap:
            length, p, s = heappop(heap)
            if p == target:
                return length

            # instruction 'A'
            new_p = p + s
            new_s = s * 2
            new_length = length + 1
            if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                dp[(new_p, new_s)] = new_length
                heappush(heap, (new_length, new_p, new_s))

            # instruction 'R', either 'RA' or 'RRA', no point of 'RRRA'
            if s > 0:
                # 'RA'
                new_p = p - 1
                new_s = -2
                new_length = length + 2
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))
                # 'RRA'
                new_p = p + 1
                new_s = 2
                new_length = length + 3
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))
            if s < 0:
                # 'RA'
                new_p = p + 1
                new_s = 2
                new_length = length + 2
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))
                # 'RRA'
                new_p = p - 1
                new_s = -2
                new_length = length + 3
                if 0 < new_p < upper and new_length < dp_helper(new_p, new_s):
                    dp[(new_p, new_s)] = new_length
                    heappush(heap, (new_length, new_p, new_s))


import math

class Solution:
    '''a very elegant solution using top-down dp.
    '''
    def __init__(self):
        self.dp = {}

    def racecar(self, target) -> int:
        if target in self.dp:
            return self.dp[target]
        
        n = int(math.log2(target + 1))
        if 2 ** n - 1 == target:
            self.dp[target] = n
            return n

        # 'A' (n + 1) times, reach 2**(n+1) - 1, surpass the target, then reverse 'R'
        self.dp[target] = (n + 1) + 1 + self.racecar(2 ** (n + 1) - 1 - target)
        
        # 'A' n times, reach 2**n, then reverse 'R', go back some distance (could be zero), then 'R' again
        for m in range(n):
            self.dp[target] = min(self.dp[target], n + 1 + m + 1 + self.racecar(target - 2**n + 2**m))
        
        return self.dp[target]

target = 4525
s = Solution()
print(s.racecar(target))



# @lc code=end

