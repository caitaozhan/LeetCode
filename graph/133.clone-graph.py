#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque

class Solution:
    '''one pass solution'''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        queue = deque([node])
        clone = {node.val: Node(node.val)}  # also act as visited
        while queue:
            cur = queue.popleft()
            for nxt in cur.neighbors:
                if nxt.val not in clone:
                    clone[nxt.val] = Node(nxt.val)
                    queue.append(nxt)
                clone[cur.val].neighbors.append(clone[nxt.val])
        return clone[1]


class Solution:
    '''two pass solution'''
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        # first bfs: set up the nodes only
        queue = deque([node])
        clone = {node.val: Node(node.val)}
        while queue:
            cur = queue.popleft()
            for nxt in cur.neighbors:
                if nxt.val not in clone:
                    queue.append(nxt)
                    clone[nxt.val] = Node(nxt.val)
        
        # second bfs: set up the connections
        queue = deque([node])
        visited = set([node.val])
        while queue:
            cur = queue.popleft()
            for nxt in cur.neighbors:
                if nxt.val not in visited:
                    queue.append(nxt)
                    visited.add(nxt.val)
                clone[cur.val].neighbors.append(clone[nxt.val])

        return clone[node.val]

# @lc code=end

