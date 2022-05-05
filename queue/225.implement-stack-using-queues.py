#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

from collections import deque

# @lc code=start
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # move q2 elements to q1, then put x to q2, then put the q1 elements to q2
        while self.q2:
            self.q1.append(self.q2.popleft())

        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

    def pop(self) -> int:
        return self.q2.popleft()

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return True if len(self.q2) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

