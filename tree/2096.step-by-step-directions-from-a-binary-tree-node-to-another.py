'''

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. 
You are also given an integer startValue representing the value of the start node s, 
and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. 
Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. 
Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(root: 'TreeNode', stack):
            if root and not (self.start_stack and self.dest_stack):
                if root.val == startValue:
                    for node in stack + [root]:
                        self.start_stack.append(node)
                if root.val == destValue:
                    for node in stack + [root]:
                        self.dest_stack.append(node)
                if self.start_stack and self.dest_stack:
                    return

                stack.append(root)     # had some issues when I put this stack.append(root) before the if root.val == startValue.
                dfs(root.left, stack)  # The return in the middle breaks the append/pop. There should be no return between the append and pop
                dfs(root.right, stack)
                stack.pop()

        # step 1: build the stack for start value and dest value
        self.start_stack = []  # the reference to a TreeNode 
        self.dest_stack = []
        dfs(root, [])

        # step 2: get the answer by the two stacks (the key is to find the lowest common node)
        i = 0
        while i < len(self.start_stack) and i < len(self.dest_stack):
            if self.start_stack[i].val == self.dest_stack[i].val:
                i += 1
            else:
                break
        low_common = i - 1
        up_length = len(self.start_stack) - 1 - low_common
        ans = 'U' * up_length
        prev = low_common
        cur = low_common + 1
        while cur < len(self.dest_stack):
            if self.dest_stack[prev].right and self.dest_stack[cur].val == self.dest_stack[prev].right.val:   # forgot to check the dest[prev].right is None
                ans += 'R'
            else:
                ans += 'L'
            prev += 1
            cur += 1
        return ans
