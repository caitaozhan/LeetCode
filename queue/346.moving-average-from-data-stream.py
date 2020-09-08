"""

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = deque(maxlen=size)
        self.summ = 0

    def next(self, val: int) -> float:
        if len(self.queue) < self.size:
            self.summ += val
            self.queue.append(val)
            return self.summ/len(self.queue)
        else:
            self.summ -= self.queue[0]
            self.summ += val
            self.queue.append(val)
            return self.summ/self.size
