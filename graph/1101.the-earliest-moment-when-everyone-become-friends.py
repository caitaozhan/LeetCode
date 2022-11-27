'''There are n people in a social group labeled from 0 to n - 1. 
You are given an array logs where logs[i] = [timestampi, xi, yi] indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a. 
Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. 
If there is no such earliest time, return -1.
'''

from typing import List

class DisjointSet:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]  # initially, the parent of a node is itself
        self.root_set = set(self.parent)

    def union(self, a: int, b: int):
        '''merge a to b
        '''
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.root_set.remove(root_a)

    def find(self, a: int) -> int:
        '''find the root of a
        '''
        cur = a
        while self.parent[cur] != cur:
            tmp_parent = self.parent[cur]
            # path compression: a -> b -> c =>  a -> b & a -> c
            self.parent[cur] = self.parent[tmp_parent]
            cur = tmp_parent
        return cur

    def check_unique_parent(self) -> bool:
        return len(self.root_set) == 1


class Solution:
    '''this is cearly a disjoint set problem
    '''
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])    # need to sort the timestamps ...
        dset = DisjointSet(n)
        for time, a, b in logs:
            dset.union(a, b)
            if dset.check_unique_parent():
                return time
        return -1


logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
n = 6

logs = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
n = 4

s = Solution()
print(s.earliestAcq(logs, n))
