#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    '''5/5/2022
    '''
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



class MyQueue:
    '''redo on 12/16/2022
       push is O(1), and pop is amortized O(1)
    '''
    def __init__(self):
        self.s_push = []
        self.s_pop = []
        self.front = None

    def push(self, x: int) -> None:
        if len(self.s_push) == 0:
            self.front = x
        self.s_push.append(x)

    def pop(self) -> int:
        if self.s_pop:                # if s_pop is not empty, then directly pop an element from it
            return self.s_pop.pop()
        else:                         # if s_pop is empty, then move the elements from s_push to s_pop
            while self.s_push:
                self.s_pop.append(self.s_push.pop())
            return self.s_pop.pop()

    def peek(self) -> int:
        if self.s_pop:
            return self.s_pop[-1]
        else:
            return self.front

    def empty(self) -> bool:
        return len(self.s_push) == 0 and len(self.s_pop) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

