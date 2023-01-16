
from typing import List
from collections import defaultdict

class Solution:
    '''do DFS at each node, O(n^2), TLE...
    '''
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # 1: build graph
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vals_dd = defaultdict(list)
        for i, val in enumerate(vals):
            vals_dd[val].append(i)
        
        self.ans = 0
        # 2: do dfs
        def dfs(cur: int, parent: int, start_idx, start_val: int) -> None:
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                if vals[nxt] > start_val:
                    continue
                if vals[nxt] == start_val:
                    if start_idx < nxt:
                        self.ans += 1
                dfs(nxt, cur, start_idx, start_val)

        for val, node_list in vals_dd.items():
            self.ans += len(node_list)               # path consisting a single node
            for node in node_list:
                dfs(node, None, node, val)

        return self.ans


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, node: int) -> int:
        cur = node
        while self.parent[cur] != cur:
            cur_parent = self.parent[cur]
            self.parent[cur] = self.parent[cur_parent]  # path compression
            cur = cur_parent
        return cur
    
    def union(self, node1: int, node2: int):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 != parent2:
            self.parent[parent1] = parent2


class Solution:
    '''use DisjointSet smartly: O(n)
       1) sort the nodes by values
       2) explore the graph iteratively from small value node to large value node
       3) at each iteration, do union to build up the connectivity. add up the answer by using the connectivity
    '''
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # 1: build graph
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        vals_dd = defaultdict(list)
        for i, val in enumerate(vals):
            vals_dd[val].append(i)

        # 2: sort the nodes by values, and do union at each interation
        n = len(vals)
        ds = DisjointSet(n)
        ans = 0
        for val, node_list in sorted(vals_dd.items()): # sorting is the key to make sure the path is a good path.
            # 2.1: do union                            # when you start discovering the graph from the node with small values, 
            for node in node_list:                     # the path in the connected component must be good
                for nxt in g[node]:
                    if vals[nxt] > vals[node]:
                        continue
                    ds.union(node, nxt)
            # 2.2: group the nodes by parent
            group_dd = defaultdict(list)
            for node in node_list:
                parent = ds.find(node)
                group_dd[parent].append(node)
            # 2.3: add up the answer
            for parent, node_list in group_dd.items():
                size = len(node_list)
                ans += size      # path with a single node
                if size >= 2:    # path with two or more nodes
                    ans += size * (size-1) // 2

        return ans

vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]

# vals = [1,3,2,1,3,3]
# edges = [[0,1],[0,2],[2,3],[2,4],[3,5]]


# print(len(vals))
# print(len(edges))

s = Solution()
print(s.numberOfGoodPaths(vals, edges))
