#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = [0] * n
        cur_sum = 0
        state = 'a'
        for i in range(n):
            if state == 'a':
                if cur_sum + 1 + (n - 1 - i) * 26 >= k:   # greedy: put 'a' where possible
                    s[i] = 'a'
                    cur_sum += 1
                else:
                    state = '*'
            if state == '*':
                tmp = k - cur_sum - (n - 1 - i) * 26      # only one char that is none 'a' or 'z'
                # cur_sum += tmp
                s[i] = chr(96 + tmp)
                state = 'z'
                continue
            if state == 'z':                              # all the rest are 'z'
                s[i] = 'z'
                # cur_sum += 26

        
        return ''.join(s)


        
# @lc code=end

