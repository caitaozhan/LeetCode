#
# @lc app=leetcode id=2013 lang=python3
#
# [2013] Detect Squares
#

from typing import List

# @lc code=start
class DetectSquares:

    def __init__(self):
        self.mydict = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point in self.mydict:
            self.mydict[point] += 1
        else:
            self.mydict[point] = 1

    def count(self, point: List[int]) -> int:
        squares = set()
        for p1 in self.mydict.keys():
            if p1[0] == point[0] and p1[1] != point[1]:   # same x value, perpendicular to the x-axis
                length = abs(point[1] - p1[1])            # length of the square
                p2 = (p1[0] - length, p1[1])
                p3 = (p2[0], point[1])
                if p2 in self.mydict and p3 in self.mydict:
                    square = tuple(sorted([p1, p2, p3]))
                    squares.add(square)
                p2 = (p1[0] + length, p1[1])
                p3 = (p2[0], point[1])
                if p2 in self.mydict and p3 in self.mydict:
                    square = tuple(sorted([p1, p2, p3]))
                    squares.add(square)
            elif p1[1] == point[1] and p1[0] != point[0]: # same y value, perpendicular to the y-axis
                length = abs(point[0] - p1[0])            # length of the square
                p2 = (p1[0], p1[1] - length)
                p3 = (point[0], p2[1])
                if p2 in self.mydict and p3 in self.mydict:
                    square = tuple(sorted([p1, p2, p3]))
                    squares.add(square)
                p2 = (p1[0], p1[1] + length)
                p3 = (point[0], p2[1])
                if p2 in self.mydict and p3 in self.mydict:
                    square = tuple(sorted([p1, p2, p3]))
                    squares.add(square)
            else:
                pass
        ans = 0
        for square in squares:
            p1, p2, p3 = square
            ans += self.mydict[p1] * self.mydict[p2] * self.mydict[p3]
        return ans

        
class DetectSquares:
    '''the previous solution considered both same x-value and same y-value and used a set to prevent duplicates...
       in this solution, only same x-value case is considered, so there are no duplicates
    '''
    def __init__(self):
        self.mydict = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point in self.mydict:
            self.mydict[point] += 1
        else:
            self.mydict[point] = 1

    def count(self, point: List[int]) -> int:
        squares = []
        for p1 in self.mydict.keys():
            if p1[0] == point[0] and p1[1] != point[1]:   # same x value, perpendicular to the x-axis
                length = abs(point[1] - p1[1])            # length of the square
                p2 = (p1[0] - length, p1[1])
                p3 = (p2[0], point[1])
                if p2 in self.mydict and p3 in self.mydict:
                    squares.append([p1, p2, p3])
                p2 = (p1[0] + length, p1[1])
                p3 = (p2[0], point[1])
                if p2 in self.mydict and p3 in self.mydict:
                    squares.append([p1, p2, p3])
        ans = 0
        for square in squares:
            p1, p2, p3 = square
            ans += self.mydict[p1] * self.mydict[p2] * self.mydict[p3]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
# @lc code=end

