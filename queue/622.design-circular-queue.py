#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.array = [0] * k
        self.start = 0
        self.end = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.array[self.end] = value
        self.end = (self.end + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.start = (self.start + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.start]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.end - 1]
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
myCircularQueue = MyCircularQueue(3);
myCircularQueue.enQueue(1)
myCircularQueue.enQueue(2)
myCircularQueue.enQueue(3)
myCircularQueue.enQueue(4)
myCircularQueue.Rear()
myCircularQueue.isFull()
myCircularQueue.deQueue()
myCircularQueue.enQueue(4)
myCircularQueue.Rear()

# @lc code=end

