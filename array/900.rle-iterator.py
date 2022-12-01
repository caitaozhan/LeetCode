#
# @lc app=leetcode id=900 lang=python3
#
# [900] RLE Iterator
#

from typing import List

# @lc code=start
class RLEIterator:
    '''Naive implementation, TLE
    '''
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        ret = None
        while n > 0:
            if self.i >= len(self.encoding):
                return -1
            if self.encoding[self.i] > 0:
                self.encoding[self.i] -= 1
                ret = self.encoding[self.i + 1]
                n -= 1
            if self.encoding[self.i] == 0:
                self.i += 2
        return ret


class RLEIterator:
    '''deduct the maximum possible value each time
    '''
    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.i = 0

    def next(self, n: int) -> int:
        ret = None
        while n > 0:
            if self.i >= len(self.encoding):
                return -1
            if self.encoding[self.i] > 0:
                minn = min(self.encoding[self.i], n)
                self.encoding[self.i] -= minn  # instead of detucting 1 at a time, detuct the min value
                n -= minn
                ret = self.encoding[self.i + 1]
            if self.encoding[self.i] == 0:
                self.i += 2
        return ret

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
# @lc code=end

