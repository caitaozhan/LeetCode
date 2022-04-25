#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

# @lc code=start
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        i = 0
        cur = self.dummy.nxt
        while cur:
            if i == index:
                break
            cur = cur.nxt
            i += 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.length += 1
        old_head = self.dummy.nxt
        new_head = Node(val, old_head)
        self.dummy.nxt = new_head

    def addAtTail(self, val: int) -> None:
        self.length += 1
        pre = self.dummy
        cur = self.dummy.nxt
        while cur:
            pre = cur
            cur = cur.nxt
        node = Node(val)
        pre.nxt = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        self.length += 1
        pre = self.dummy
        cur = self.dummy.nxt
        i = 0
        while cur:
            if i == index:
                break
            pre = cur
            cur = cur.nxt
            i += 1
        new_node = Node(val, cur)
        pre.nxt = new_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None
        self.length -= 1
        pre = self.dummy
        cur = self.dummy.nxt
        i = 0
        while cur:
            if i == index:
                break
            pre = cur
            cur = cur.nxt
            i += 1
        pre.nxt = cur.nxt


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

