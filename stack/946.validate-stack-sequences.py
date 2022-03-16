#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0    # for pushed
        j = 0    # for popped
        while i < len(pushed):
            stack.append(pushed[i])
            i += 1
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return True if len(stack) == 0 else False


class Solution:
    '''same complexity but faster runtime'''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return len(stack) == 0

# @lc code=end

