#
# @lc app=leetcode id=282 lang=python3
#
# [282] Expression Add Operators
#

from typing import List

# @lc code=start
class Solution:
    '''O(n*4**n), TLE
    '''
    def check(self, s: str) -> bool:
        if s[0] == '0':
            if 1 < len(s) and s[1].isdigit():
                return False
        for i in range(1, len(s)-1):
            if s[i] == '0':
                if s[i+1].isdigit() and s[i-1].isdigit() is False:
                    return False
        return True

    def generate_expressions(self, idx: int):
        if idx == len(self.num_list) - 1:
            expression = ''.join(self.num_list)
            if self.check(expression):
                self.expressions.append(expression)
            return

        if self.num_list[idx].isdigit():
            self.generate_expressions(idx + 1)
        else:
            for ch in ['+', '-', '*', '']:
                self.num_list[idx] = ch
                self.generate_expressions(idx + 1)

    def evaluate(self, s: str) -> int:
        cur_num = 0
        prev_operator = '+'
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                cur_num = cur_num * 10 + int(s[i])
            if s[i].isdigit() is False or i == len(s) - 1:
                if prev_operator == '+':
                    stack.append(cur_num)
                elif prev_operator == '-':
                    stack.append(-cur_num)
                else:  # prev_operator == '*'
                    prev_number = stack.pop()
                    stack.append(prev_number * cur_num)
                cur_num = 0
                prev_operator = s[i]
        return sum(stack)


    def addOperators(self, num: str, target: int) -> List[str]:
        # step 1: process num
        self.num_list = []
        for i in range(len(num) - 1):
            self.num_list.append(num[i])
            self.num_list.append('')
        self.num_list.append(num[-1])

        # step 2: generate all the expressions
        self.expressions = []
        self.generate_expressions(idx=0)

        # step 3: evaluate all the expressions
        ans = []
        for expression in self.expressions:
            if self.evaluate(expression) == target:
                ans.append(expression)
        return ans


class Solution:
    '''O(4*n)
    '''
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        def recurse(index, prev_operand, current_operand, value, string):
            # Done processing all the digits in num
            if index == N:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return

            # Extending the current operand by one digit
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)
            # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
            # valid operand. Hence this check
            if current_operand > 0:
                # NO OP recursion
                recurse(index + 1, prev_operand, current_operand, value, string)
            # ADDITION
            string.append('+')
            string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop()
            string.pop()
            # Can subtract or multiply only if there are some previous operands
            if string:
                # SUBTRACTION
                string.append('-')
                string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop()
                string.pop()
                # MULTIPLICATION
                string.append('*')
                string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop()
                string.pop()

        N = len(num)
        answers = []
        recurse(0, 0, 0, 0, [])    
        return answers


num = '123'
target = 6

# num = "105"
# target = 5

# num = "1009"
# target = 9

# num = "2147483647"
# target = 2147483647

# num = "00"
# target = 0

s = Solution()
print(s.addOperators(num, target))

# @lc code=end


