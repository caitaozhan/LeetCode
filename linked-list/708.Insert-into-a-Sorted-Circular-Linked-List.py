"""

Given a node from a Circular Linked List which is sorted in ascending order, write a function to insert a value insertVal into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

 

Example 1:


 
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.



Example 2:

Input: head = [], insertVal = 1
Output: [1]
Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.
Example 3:

Input: head = [1], insertVal = 0
Output: [1,0]
 

Constraints:

0 <= Number of Nodes <= 5 * 10^4
-10^6 <= Node.val <= 10^6
-10^6 <= insertVal <= 10^6

"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    '''corner cases such as [3,3,3] 0 and [3,3,5] 1
    '''
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if head is None:
            head = Node(insertVal, None)
            head.next = head
            return head
        
        if head.next == head:
            node = Node(insertVal, head)
            head.next = node
            return head
        
        dummy = Node(float('inf'), head)
        pre, cur = dummy, head
        pre_min, cur_min = pre, cur # test case: [3,3,3]  0
        minn = float('inf')
        pre_hit_head = 0
        while True:
            # print(cur.val)
            if pre == head:
                pre_hit_head += 1
            if (cur.val < minn and pre_hit_head != 0) or (cur.val == minn and cur == head): # when the head is the minimum value
                minn = cur.val
                pre_min, cur_min = pre, cur
                # print(cur_min.val, pre_min.val)
            if pre.val <= insertVal <= cur.val:
                node = Node(insertVal, cur)
                pre.next = node
                return dummy.next
            if pre_hit_head == 2:
                break
            pre, cur = cur, cur.next
            
        # insert the node before the minimal node
        node = Node(insertVal, cur_min)
        pre_min.next = node
        return dummy.next
