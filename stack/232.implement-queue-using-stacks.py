#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # move s2 elements to s1, put x to s2, move s1 elements back to s1
        while self.s2:
            self.s1.append(self.s2.pop())

        self.s2.append(x)

        while self.s1:
            self.s2.append(self.s1.pop())

    def pop(self) -> int:
        return self.s2.pop()

    def peek(self) -> int:
        return self.s2[-1]

    def empty(self) -> bool:
        return True if len(self.s2) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

