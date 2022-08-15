#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mydict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        i = 0
        n = len(s)
        while i < n:
            cur = s[i]
            if i == n - 1:
                ans += mydict[cur]
                i += 1
            else: # i < n - 1:
                nxt = s[i + 1]
                if mydict[cur] >= mydict[nxt]:
                    ans += mydict[cur]
                    i += 1
                else:
                    ans += mydict[nxt] - mydict[cur]
                    i += 2
        return ans

s = 'III'
s = "LVIII"
s = "MCMXCIV"
so = Solution()
print(so.romanToInt(s))


# @lc code=end

