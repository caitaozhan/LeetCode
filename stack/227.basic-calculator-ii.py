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



class Solution:
    '''use only one stack. remove '-' by turning -a into +(-a), use a variable to store the current operator
    '''
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        cur_num = 0
        prev_operation = '+' if s[0] != '-' else '-'
        i = 0
        for i in range(len(s)):
            if s[i].isdigit():
                cur_num = 10*cur_num + int(s[i])
            if s[i].isdigit() is False or i == len(s) - 1:
                if prev_operation == '+':
                    stack.append(cur_num)
                elif prev_operation == '-':
                    stack.append(-cur_num)
                elif prev_operation == '*':
                    prev_num = stack.pop()
                    stack.append(prev_num * cur_num)
                elif prev_operation == '/':
                    prev_num = stack.pop()
                    stack.append(int(prev_num / cur_num))
                prev_operation = s[i]
                cur_num = 0
        ans = 0
        while stack:
            ans += stack.pop()        # only addition in the stack
        return ans



string = "3+2*2"
string = "1-1+1"
string = "3/2"
string = " 3+5 / 2 - 1"
s = Solution()
print(s.calculate(string))

# @lc code=end

