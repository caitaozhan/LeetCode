#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # deal with the sign
        neg = 0
        if dividend < 0:
            neg += 1
            dividend = -dividend
        if divisor < 0:
            neg += 1
            divisor = -divisor

        def divide_by_add(a: str, b: str) -> (str, str):
            ''' a / b
            Return:
                quotient, remainder
            '''
            a = int(a)
            b = int(b)
            counter = 0
            summ = 0
            while summ < a:
                summ += b
                counter += 1
            if summ > a:
                summ -= b
                counter -= 1
            return str(counter), str(a - summ)

        ans = ''
        dividend = str(dividend)
        i = 0
        r = ''
        while i < len(dividend):
            j = 1
            a = r + dividend[i:i+j]
            q, tmp_r = divide_by_add(a, divisor)
            while q == '0':
                j += 1
                if i+j > len(dividend):
                    break
                a = r + dividend[i:i+j]
                q, tmp_r = divide_by_add(a, divisor)
            r = tmp_r
            if q == '0':  # the break
                ans += '0'*(j-1)
            else:
                ans += '0'*(j-1) + q
            i += j

        ans = -int(ans) if neg == 1 else int(ans)
        if ans > (1<<31) - 1:
            ans = (1<<31) - 1
        elif ans < -(1<<31):
            ans = -(1<<31)
        return ans

# dividend = 413
# divisor = 3
# dividend = 113
# divisor = 3
# dividend = 0
# divisor = -1
# dividend = 10
# divisor = 3
# dividend = 1
# divisor = 1
# dividend = -2147483648
# divisor = -1
# dividend = 2147483647
# divisor = 2
dividend = -1060849722
divisor = 99958928
s = Solution()
print(s.divide(dividend, divisor))

# @lc code=end

