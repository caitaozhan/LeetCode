#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # step 1: build graph
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        # step 2: do DFS with explicit stack
        colors = {}
        for start in range(1, n+1):
            if start in colors:
                continue
            colors[start] = 0
            stack = [start]
            while stack:
                cur = stack.pop()
                for nxt in graph[cur]:
                    if nxt not in colors:
                        colors[nxt] = colors[cur] ^ 1
                        stack.append(nxt)
                    else:  # already colored
                        if colors[nxt] == colors[cur]:
                            return False
        return True



        
# @lc code=end

