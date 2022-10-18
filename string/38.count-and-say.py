#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def convert(self, s: str) -> str:
        mylist = []
        i, j = 0, 0
        while i < len(s):
            if j < len(s) and s[i] == s[j]:
                j += 1
            else:
                mylist.append(f'{j - i}{s[i]}')
                i = j
        return ''.join(mylist)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.convert(self.countAndSay(n - 1))



import re

class Solution:
    def convert(self, s: str) -> str:
        return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.convert(self.countAndSay(n - 1))

# s = '11122211'
# print(re.findall(r'(.)\1*', s))
# m = re.search(r'(.)\1*', s)
# print(m.group(0))
# print(m.group(1))



n = 4
s = Solution()
print(s.countAndSay(n))

# @lc code=end

