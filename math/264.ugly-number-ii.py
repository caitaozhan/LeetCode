#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    '''naive method, TLE for large n'''
    def nthUglyNumber(self, n: int) -> int:
        def is_ugly(n: int) -> bool:
            while n % 2 == 0:
                n //= 2
            while n % 3 == 0:
                n //= 3
            while n % 5 == 0:
                n //= 5
            return n == 1

        counter = 0
        i = 1
        while True:
            if is_ugly(i):
                counter += 1
                if counter == n:
                    return i
            i += 1

class Solution:
    '''dp with O(n^2), but still TLE'''
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        while len(dp) < n:
            cur_max = dp[-1]
            next = float('inf')
            for num in dp:
                for factor in [2, 3, 5]:
                    new_num = num * factor
                    if new_num > cur_max:
                        next = min(next, new_num)
            dp.append(next)
        return dp[-1]


class Solution:
    '''dp with O(n)'''
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2, i3, i5 = 0, 0, 0
        while len(dp) < n:
            nxt = min(dp[i2] * 2 , dp[i3] * 3, dp[i5] * 5)
            if dp[i2] * 2 == nxt:
                i2 += 1
            if dp[i3] * 3 == nxt:
                i3 += 1
            if dp[i5] * 5 == nxt:
                i5 += 1
            dp.append(nxt)
        return dp[-1]


n = 20
s = Solution()
print(s.nthUglyNumber(n))


########### One time precomputation, O(n)
class Ugly:
    '''dp with O(n)'''
    def __init__(self):
        self.dp = [1]
        i2, i3, i5 = 0, 0, 0
        while len(self.dp) < 1690:
            next = min(self.dp[i2] * 2 , self.dp[i3] * 3, self.dp[i5] * 5)
            if self.dp[i2] * 2 == next:
                i2 += 1
            if self.dp[i3] * 3 == next:
                i3 += 1
            if self.dp[i5] * 5 == next:
                i5 += 1
            self.dp.append(next)

class Solution:
    ugly = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return Solution.ugly.dp[n-1]
###########


########### One time precomputation, O(n^2)
class Ugly:
    def __init__(self):
        self.dp = [1]
        while len(self.dp) < 1690:
            cur_max = self.dp[-1]
            next = float('inf')
            for num in self.dp:
                for factor in [2, 3, 5]:
                    new_num = num * factor
                    if new_num > cur_max:
                        next = min(next, new_num)
            self.dp.append(next)

class Solution:
    ugly = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return Solution.ugly.dp[n-1]
###########


from heapq import heappush, heappop

class Solution:
    '''using a heap, O(n*logn)'''
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        mylist = []
        seen = set(h)
        while len(mylist) < n:
            num = heappop(h)
            mylist.append(num)
            for factor in [2, 3, 5]:
                new_num = num * factor
                if new_num not in seen:
                    heappush(h, new_num)
                    seen.add(new_num)
        return mylist[-1]

n = 10
s = Solution()
print(s.nthUglyNumber(n))
# @lc code=end

