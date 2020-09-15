#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        num_stack = []
        sym_stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit() is False:
                if s[i] == ')':     # do something when met ')'
                    self.process_parentheses(num_stack, sym_stack)
                else:
                    sym_stack.append(s[i])
                i += 1
            else:
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                if sym_stack and sym_stack[-1] == '-':
                    num_stack.append(-int(num))
                    sym_stack[-1] = '+'
                else:
                    num_stack.append(int(num))
        self.process(num_stack, sym_stack)
        return num_stack[-1]

    def process_parentheses(self, num_stack, sym_stack):
        while sym_stack[-1] != '(':
            b = num_stack.pop()
            a = num_stack.pop() if num_stack else 0
            sym = sym_stack.pop()
            if sym == '+':
                a = a + b
            else:
                a = a - b
            num_stack.append(a)
        sym_stack.pop()
        if sym_stack and sym_stack[-1] == '-':
            num_stack[-1] = -num_stack[-1]
            sym_stack[-1] = '+'

    def process(self, num_stack, sym_stack):
        while sym_stack:
            b = num_stack.pop()
            a = num_stack.pop() if num_stack else 0
            sym = sym_stack.pop()
            if sym == '+':
                a = a + b
            else:
                a = a - b
            num_stack.append(a)


def test():
    # s = "(10+(4+5+2)-3)+ (6+8)"
    # s = "1 + 1"
    # s = " (-2-1) + 2 "
    s = "(7)-(0)+(4)"
    so = Solution()
    print(so.calculate(s))

test()

# @lc code=end

