'''

Stream of coordinates. Return all the squares that exists.

Example:
(1, 2)	
    return False
(3, 5)
    return False
(1, 5)	
    return False
(4, 2)
    return False
(4, 5)
    return a square [(1, 2), (1, 5), (4, 5), (4, 2)]

'''


class Squares:
    '''a smart O(n) solution
    '''
    def __init__(self):
        self.points = set()
    
    def other_two_points(self, p1, p):
        mid_p   = ((p1[0] + p[0]) / 2,  (p1[1] + p[1]) / 2)
        delta_x = (p[1] - p1[1]) / 2
        delta_y = (p[0] - p1[0]) / 2
        p2 = (mid_p[0] - delta_x, mid_p[1] + delta_y)
        p3 = (mid_p[0] + delta_x, mid_p[1] - delta_y)
        return p2, p3

    def get_all_squares(self, p):
        squares = []
        for p1 in self.points:
            p2, p3 = self.other_two_points(p1, p)
            if p2 in self.points and p3 in self.points:
                squares.append([p, p1, p2, p3])
        self.points.add(p)
        return False if len(squares) == 0 else squares


def test():
    mysquare = Squares()
    p = (1, 2)
    print(f'{p} -> {mysquare.get_all_squares(p)}')
    p = (3, 5)
    print(f'{p} -> {mysquare.get_all_squares(p)}')
    p = (1, 5)
    print(f'{p} -> {mysquare.get_all_squares(p)}')
    p = (4, 2)
    print(f'{p} -> {mysquare.get_all_squares(p)}')
    p = (4, 5)
    print(f'{p} -> {mysquare.get_all_squares(p)}')


test()
