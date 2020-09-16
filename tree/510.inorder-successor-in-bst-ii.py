'''

Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
 

Follow up:

Could you solve it without looking up any of the node's values?

 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Example 3:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17
Example 4:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15
Example 5:

Input: tree = [0], node = 0
Output: null
 

Constraints:

-10^5 <= Node.val <= 10^5
1 <= Number of Nodes <= 10^4
All Nodes will have unique values.

'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution2:

    def most_left(self, root):
        '''return the most left node in the tree'''
        cur = root
        while cur.left:
            cur = cur.left
        return cur

    def find_larger_parent(self, root, val):
        '''find a parent whose value is larger than root's val. If there is no such parent, then return None'''
        cur = root
        while cur.parent:
            cur = cur.parent
            if cur.val > val:
                return cur
        return None

    def inorderSuccessor(self, node: Node) -> Node:
        if node is None:
            return None
        if node.right is not None:
            return self.most_left(node.right)
        else:
            larger_parent = self.find_larger_parent(node, node.val)
            if larger_parent is None:
                return None
            else:
                return larger_parent


class Solution:
    '''
        Follow up:
        Could you solve it without looking up any of the node's values?
    '''
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        if node.right is not None:
            return self.most_left(node.right)
        else:
            larger_parent = self.find_larger_parent(node)
            return larger_parent if larger_parent is not None else None
        
    def most_left(self, root):
        cur = root
        while cur.left:
            cur = cur.left
        return cur
    
    def find_larger_parent(self, node):
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
        return parent

''' 
root = 
{
    "$id":"1", 
    "left":{"$id":"2","left":null,"parent":{"$ref":"1"},"right":null,"val":1},
    "parent":null,
    "right":{"$id":"3","left":null,"parent":{"$ref":"1"},"right":null,"val":3},
    "val":2
}
'''