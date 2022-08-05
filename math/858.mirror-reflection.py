#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#

# @lc code=start
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        n = 1
        while True:
            if n % 2 == 1:        # n is odd, hits right side mirror
                y = (n*q) % p     # y is the y axis value when it hits right side mirror
                if y == 0:
                    if ((n*q) // p) % 2 == 1:
                        return 1
                    else:
                        return 0
            else:                 # n is even, hits left side mirror
                y = p - (n*q) % p # y is the y axis value when it hits left side mirror
                if y == p:
                    return 2
            n += 1

p = 5
q = 4
p = 2
q = 1
s = Solution()
print(s.mirrorReflection(p, q))

# @lc code=end

