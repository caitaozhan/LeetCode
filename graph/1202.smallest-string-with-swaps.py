#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

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
    '''Claim: when some nodes (index of string) are connected, 
              then the associated chars can be minimized to sorting.
    '''
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        ds = DS(n)
        for a, b in pairs:
            ds.union(a, b)
        
        connected = defaultdict(list)
        for i in range(n):
            parent = ds.find(i)
            connected[parent].append(i)
        
        ans = [0] * n
        for _, nodes in connected.items():
            tmp = [s[i] for i in nodes]
            tmp.sort()
            j = 0
            for i in nodes:
                ans[i] = tmp[j]
                j += 1
        
        return ''.join(ans)
        


# @lc code=end

