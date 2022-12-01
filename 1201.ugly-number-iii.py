#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#

# @lc code=start


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a: int, b: int) -> int:
            '''euclidean algorithm'''
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
        
        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        # step 1: build the cycle (mylist)
        abc = sorted([a, b, c])
        a, b, c = abc[0], abc[1], abc[2]
        tmp = lcm(a, b)
        least_common_multiple = lcm(tmp, c)
        myset = set()
        i = 1
        while i * a <= least_common_multiple:
            myset.add(i * a)
            i += 1
        i = 1
        while i * b <= least_common_multiple:
            myset.add(i * b)
            i += 1
        i = 1
        while i * c <= least_common_multiple:
            myset.add(i * c)
            i += 1
        mylist = sorted(list(myset))
        T = len(mylist)

        # step 2: compute the answer
        period = n // T
        remainder = n % T
        ans = mylist[remainder-1] + period * least_common_multiple

        return ans

# n, a, b, c = 5, 2, 11, 13
n, a, b, c = 25, 2, 3, 5
s = Solution()
print(s.nthUglyNumber(n, a, b, c))

# @lc code=end

