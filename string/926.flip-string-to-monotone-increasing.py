#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

import time

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        def remove_zero_prefix(s):
            ''' 0011 --> 11 
            Return:
                str -- the str after zero prefix removed
                int -- how many zero removed
            '''
            index = s.find('1')
            if index == -1:
                return '', 0
            else:
                return s[index:], index


        zero_current = s.count('0')
        flip_one2zero = 0
        ans = float('inf')
        while len(s) > 0:
            s, zero_removed = remove_zero_prefix(s)
            if len(s) == 0:
                ans = min(ans, flip_one2zero)
                break

            # now the first char is '1'
            # rest is all '1'
            zero_left = zero_current - zero_removed
            flip_zero2one = zero_left
            ans = min(ans, flip_one2zero + flip_zero2one)

            # flip the first char from '1' to '0'
            s = '0' + s[1:]  # NOTE string is a constant, cannot s[0] = '1'
            zero_current = zero_left + 1
            flip_one2zero += 1

        return ans


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero_left = s.count('0')
        s = list(s)
        flip_one2zero = 0
        ans = float('inf')
        i = 0
        while i < len(s):
            if s[i] == '0':
                i += 1
                zero_left -= 1
                continue
            # now the first char is '1'
            
            # case 1: flip all the '0' left to '1'
            flip_zero2one = zero_left
            ans = min(ans, flip_one2zero + flip_zero2one)

            # case 2: flip the first '1' to '0'
            s[i] = '0'
            flip_one2zero += 1
            zero_left += 1

        ans = min(ans, flip_one2zero)
        return ans


class Solution:
    '''note that for a string length of 4, the end goals is has 5 possibilities:
       0000, 0001, 0011, 0111, 1111
       there will be threshold between 0 and 1
       the problem will be reduces to counting the number of 1s
       which can be done by prefix sum array in constant time
    '''
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        prefix_sum = [0] * n
        prefix_sum[0] = 1 if s[0] == '1' else 0
        for i in range(1, len(s)):
            prefix_sum[i] = prefix_sum[i-1] + int(s[i])
        
        ans = n - prefix_sum[n-1]  # turn all '0' into '1'
        for i in range(len(s)):
            flip_one2zero = prefix_sum[i]
            flip_zero2one = (n - 1 - i) - (prefix_sum[n-1] - prefix_sum[i])
            ans = min(ans, flip_one2zero + flip_zero2one)

        return ans



