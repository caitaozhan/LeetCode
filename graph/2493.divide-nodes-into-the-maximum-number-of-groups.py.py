'''

You are given a positive integer n representing the number of nodes in an undirected graph. 
The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that 
there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group
with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. 
Return -1 if it is impossible to group the nodes with the given conditions.

'''


from typing import List


class DS:
    '''disjoint set
    '''
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(self.n)]

    def find(self, a):
        while a != self.parent[a]:
            a_p = self.parent[a]
            self.parent[a] = self.parent[a_p]  # path compression
            a = a_p
        return a

    def union(self, a, b):
        a_p = self.find(a)
        b_p = self.find(b)
        if a_p != b_p:
            self.parent[a_p] = b_p  # b's root is the new root


from collections import defaultdict

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def count_layers(start: int) -> int:
            queue = [start]
            layer = {start: 1}
            while queue:
                new_queue = []
                for node in queue:
                    for nxt in g[node]:
                        if nxt not in layer:
                            layer[nxt] = layer[node] + 1
                            new_queue.append(nxt)
                        else:
                            if abs(layer[node] - layer[nxt]) != 1:
                                return -1
                queue = new_queue
            return max(layer.values())

        # step 1: use a disjoint set to find out all the disconnected parts
        g = defaultdict(list)
        ds = DS(n + 1)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
            ds.union(a, b)
        disjoints = defaultdict(list)
        for i in range(1, n + 1):
            root = ds.find(i)
            disjoints[root].append(i)
        
        # step 2: for each disconnected part, start a bfs at each node
        ans = 0
        for _, disjoint in disjoints.items():
            ans_disjoint = 0
            for node in disjoint:
                tmp = count_layers(node)
                if tmp == -1:
                    return -1
                else:
                    ans_disjoint = max(ans_disjoint, tmp)
            ans += ans_disjoint
        return ans


n = 6
edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]

n = 3
edges = [[1,2],[2,3],[3,1]]
s = Solution()
print(s.magnificentSets(n, edges))