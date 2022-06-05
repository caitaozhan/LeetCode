'''
1088. Confusing Number II

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return the number of confusing numbers in the inclusive range [1, n].

'''

class Solution:
    def __init__(self):
        self.ans = 0
        self.length = 0

    def confusingNumberII(self, n: int) -> int:

        def backtrack(index):
            if index == self.length:
                num = int(''.join(numlist))
                if num <= n:
                    leadingzero = 0
                    while leadingzero < self.length-1 and numlist[leadingzero] == '0':
                        leadingzero += 1
                    numlist180 = numlist[leadingzero:n]
                    numlist180.reverse()
                    for i in range(len(numlist180)):
                        numlist180[i] = digit180[numlist180[i]]
                    num180 = int(''.join(numlist180))
                    if num != num180:
                        self.ans += 1
                return

            for d in digit:
                numlist[index] = d
                # prune
                if int(''.join(numlist)) > n:
                    break
                backtrack(index + 1)
                numlist[index] = '0'


        self.length = len(str(n))
        numlist  = ['0'] * self.length
        digit    = ['0', '1', '6', '8', '9']
        digit180 = {'0':'0', '1':'1', '9':'6', '8':'8', '6':'9'}
        backtrack(index=0)
        return self.ans

n = 10**8
s = Solution()
print(s.confusingNumberII(n))

