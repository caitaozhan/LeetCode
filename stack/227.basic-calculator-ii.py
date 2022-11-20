#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        num_stack = []
        sym_stack = []
        i = 0
        # step 1: one pass and deal with '*' and '/'
        while i < len(s):
            if s[i].isdigit():
                num = s[i]
                i += 1
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                num = int(num)
                if sym_stack and (sym_stack[-1] == '*' or sym_stack[-1] == '/'):
                    operator = sym_stack.pop()
                    num2 = num_stack.pop()
                    if operator == '*':
                        num_stack.append(num * num2)
                    else:
                        num_stack.append(int(num2 / num))
                else:
                    num_stack.append(int(num))
            else:
                sym_stack.append(s[i])
                i += 1
        # step 2: now deal with '+' and '-', the key is to reverse the two stacks, because '-' is not associative
        num_stack.reverse()
        sym_stack.reverse()
        while sym_stack:
            a = num_stack.pop()
            b = num_stack.pop()
            operator = sym_stack.pop()
            if operator == '+':
                num_stack.append(a + b)
            else:
                num_stack.append(a - b)
        return num_stack[-1]


string = "3+2*2"
string = "1-1+1"
s = Solution()
print(s.calculate(string))

# @lc code=end

