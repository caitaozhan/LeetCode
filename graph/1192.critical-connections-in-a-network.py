#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

from collections import defaultdict
from typing import List

# @lc code=start
class Solution:
    '''There is a standard algo for this problem: Tarjan
       Here, we instead try to adapt the standard DFS: we reduce the problem into finding cycles
       if we exclude all the edges that are in some cycles, then the rest of the edges are the bridges
    '''
    def min_max(self, a, b):
        return (a, b) if a < b else (b, a)

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        conndict = {}
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            conndict[self.min_max(a, b)] = False   # is not part of cycle
        
        rankdict = {}
        def dfs(cur: int, rank: int) -> int:
            '''
            Args:
                cur -- the id of the cur node
                rank -- the rank or depth of the recurrsion tree
            Return:
                the minimum rank of all nodes that cur node can reach in the following DFS
                NOTE: this returned value is the key to efficiently remove the edge in cycles without redundancy
            '''
            rankdict[cur] = rank
            min_rank = float('inf')  # the returned value
            for neigh in graph[cur]:
                if neigh not in rankdict:       # unvisited node
                    neigh_rank = dfs(neigh, rank + 1)
                    if neigh_rank <= rank:
                        conndict[self.min_max(cur, neigh)] = True
                else:
                    if rankdict[neigh] == rank - 1:    # skip parent node
                        continue
                    neigh_rank = rankdict[neigh]
                    if neigh_rank < rank:   # cycle detected
                        conndict[self.min_max(cur, neigh)] = True
                min_rank = min(min_rank, neigh_rank)
            return min_rank

        dfs(cur=0, rank=0)

        ans = []
        for key, val in conndict.items():
            if val is False:
                ans.append(key)
        return ans


n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

n = 6
# connections = [[0,1],[1,2],[2,0],[1,3],[3,4],[3,5],[4,5],[0,5]]
connections = [[0,1],[1,2],[2,0],[1,3],[3,4],[3,5],[4,5]]

s = Solution()
print(s.criticalConnections(n, connections))
        

        
# @lc code=end

