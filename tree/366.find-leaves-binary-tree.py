'''
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]

'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root, leaves):
            '''if root is a leaf, then append to leaves and return True
            '''
            if root is None:
                return False
            if root.left is None and root.right is None:
                leaves.append(root.val)
                return True
            
            is_leaf = dfs(root.left, leaves)
            if is_leaf:
                root.left = None
            is_leaf = dfs(root.right, leaves)
            if is_leaf:
                root.right = None
            
            return False
        
        is_leaf = False
        ans = []
        while not is_leaf:
            leaves = []
            is_leaf = dfs(root, leaves)
            ans.append(leaves)
        return ans


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def dfs(root):
            if root is None:
                return -1
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            root_height = max(left_height, right_height) + 1
            mydict[root_height].append(root.val)
            return root_height
            
        mydict = defaultdict(list)  # hight --> [val, ...]
        dfs(root)
        ans = []
        for key in sorted(mydict.keys()):
            ans.append(mydict[key])
        return ans