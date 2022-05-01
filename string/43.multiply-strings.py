#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

from itertools import zip_longest

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def get_ten_single(num):
            single = num % 10
            ten = num // 10
            return ten, single
        
        # step 1: multiply
        results = []
        len1 = len(num1)
        len2 = len(num2)
        for i_ in range(len2):
            i = len2 - 1 - i_
            cur = [0] * i_
            carry = 0
            for j_ in range(len1):
                j = len1 - 1 - j_
                prod = int(num2[i]) * int(num1[j])
                ten, single = get_ten_single(prod + carry)
                cur.append(single)
                carry = ten
            if carry > 0:
                cur.append(carry)   # BUG: forgot this step
            results.append(cur)
                
        # step 2: addition
        ans = results.pop()
        for num in results:
            new_ans = []
            carry = 0
            for d1, d2 in zip_longest(ans, num, fillvalue=0):
                ten, single = get_ten_single(d1 + d2 + carry)
                new_ans.append(single)
                carry = ten
            if carry > 0:
                new_ans.append(carry)
            ans = new_ans

        while len(ans) > 1 and ans[-1] == 0:  # BUG: delete leading zeros
            ans.pop()
        ans.reverse()
        return ''.join(map(str, ans))


# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         return str(int(num1) * int(num2))


s1 = "9133"
s2 = "0"
s = Solution()
print(s.multiply(s1, s2))

        
# @lc code=end
