
from collections import defaultdict

class Solution:
    '''turn a string problem into a graph problem and use DFS
    '''
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # 1: build graph
        not_visited = set()
        g = defaultdict(list)
        for c1, c2 in zip(s1, s2):
            g[c1].append(c2)
            g[c2].append(c1)
            not_visited.add(c1)
            not_visited.add(c2)

        # 2: dfs
        def dfs(node: str, group: set):
            for nxt in g[node]:
                if nxt in not_visited:
                    not_visited.remove(nxt)
                    group.add(nxt)
                    dfs(nxt, group)

        groups = []
        all_char = list(not_visited)
        for ch in all_char:
            if ch in not_visited:
                not_visited.remove(ch)
                group = set([ch])
                dfs(ch, group)
                groups.append(group)
        
        # 3: get the anwser
        ans = []
        for ch in baseStr:
            for group in groups:
                if ch in group:
                    ans.append(min(group))
                    break
            else:
                ans.append(ch)
        return ''.join(ans)



s1 = "parker"
s2 = "morris"
baseStr = "parser"

s1 = "hello"
s2 = "world"
baseStr = "hold"

s = Solution()
print(s.smallestEquivalentString(s1, s2, baseStr))