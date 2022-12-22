#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    '''a beautiful solution from Leetcode's solution
       to find a O(n) solution, the key is finding the relationships between ans[i] and ans[j] (not easy to find)
       to find the relationship, analyse a edge, and cut the edge, i.e., the tree is split into two halves.
       ans[i] is the left half (child) and ans[j] is the right half (current node)
    '''
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # step 1: build the graph
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        # step 2: post order traversal -- deal with the childs frist, then myself
        def postorder(node: int, parent: int):
            for child in g[node]:
                if child != parent:
                    postorder(child, node)
                    count[node] += count[child]
                    stsum[node] += stsum[child] + count[child]
        
        # step 3: pre order traversal -- deal with myself first, then childs
        def preorder(node: int, parent: int):
            for child in g[node]:
                if child != parent:
                    ans[child] = ans[node] + (n - count[child]) - count[child]
                    preorder(child, node)

        # assume the root is node 0
        root = 0
        count = [1] * n    # count[i] is the number of nodes in subtree-i
        stsum = [0] * n    # stsum[i] is the sum of distances from node i to all the child nodes in subtree-i
        postorder(node=root, parent=None)
        ans = [0] * n
        ans[root] = stsum[root]
        preorder(node=root, parent=None)
        return ans

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
s = Solution()
print(s.sumOfDistancesInTree(n, edges))
        
# @lc code=end

