#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

from typing import List

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(num1: str, num2: str, op: str) -> str:
            if op == '+':
                num = int(num1) + int(num2)
            elif op == '-':
                num = int(num1) - int(num2)
            elif op == '/':
                num = int(int(num1) / int(num2))
            else:
                num = int(num1) * int(num2)
            return str(num)

        stack = []
        for t in tokens:
            if len(t) == 1 and t in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                num = helper(num1, num2, t)
                stack.append(num)
            else:
                stack.append(t)
        return int(stack[0])


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = Solution()
print(s.evalRPN(tokens))

# @lc code=end

