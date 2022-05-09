#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mydict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],\
                  '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        def dfs(ans, stack, digits, i):
            if i == len(digits):
                if i > 0:
                    ans.append(''.join(stack.copy()))
                return
            for char in mydict[digits[i]]:
                dfs(ans, stack + [char], digits, i+1)

        stack = []
        ans = []
        dfs(ans, stack, digits, 0)
        return ans

# @lc code=end

