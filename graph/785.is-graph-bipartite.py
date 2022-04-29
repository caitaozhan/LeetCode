#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
from typing import List

class Solution:
    # The edge cases are when the graph is not a single connnected component...
    # So every individual connected components needs to bipartite
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        for i in range(len(graph)):
            if graph[i] and visited[i] == 0:
                result = self.bfs(i, visited, graph)
                if result is False:
                    return False
        return True

    def bfs(self, start, visited, graph):
        layer = 0
        queue = [start]
        sets = [set(), set()]        # a set for each partition
        sets[0].add(start)
        while queue:
            new_queue = []
            for cur in queue:
                for nxt in graph[cur]:
                    if visited[nxt] == 1:
                        if nxt in sets[layer]:      # connecting to a node in the same layer
                            return False
                    else:
                        new_queue.append(nxt)
                        visited[nxt] = 1
                        sets[(layer + 1) % 2].add(nxt)  # nxt belongs to the next layer
            layer = (layer + 1) % 2
            queue = new_queue
        return True


class Solution:
    '''this BFS saves memory/time comparing to the previous BFS.
    '''
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)
        for i in range(len(graph)):
            if colors[i] == -1:
                if self.bfs(graph, i, colors) is False:
                    return False
        return True
    
    def bfs(self, graph, start, colors):
        '''a layer-by-layer BFS
           return False if not bipartite, True if bipartite
        '''
        queue = [start]
        color = 0
        colors[start] = color
        while queue:
            new_queue = []
            for cur in queue:
                for nxt in graph[cur]:
                    if colors[nxt] == -1:   # not colored
                        colors[nxt] = (color + 1) % 2
                        new_queue.append(nxt)
                    else:                   # colored
                        if colors[nxt] == color:
                            return False
            queue = new_queue
            color = (color + 1) % 2
        return True

# @lc code=end


'''

[[1,3],[0,2],[1,3],[0,2]]
[[1,2,3], [0,2], [0,1,3], [0,2]]
[[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
[[4],[],[4],[4],[0,2,3]]
[[1],[0],[4],[4],[2,3]]

'''
