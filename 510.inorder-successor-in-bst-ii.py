'''

'''

# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:

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