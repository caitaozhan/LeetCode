#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import random


class SolutionNaive:
    '''naive solution
    '''
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.cur = head
        self.cur_index = 0
        self.length = self.get_length(self.head)

    def get_length(self, head: Optional[ListNode]) -> int:
        length = 0
        cur = head
        while cur is not None:
            length += 1
            cur = cur.next
        return length

    def getRandom(self) -> int:
        rand_index = random.randint(0, self.length-1)
        if rand_index >= self.cur_index:
            while self.cur_index < rand_index:
                self.cur = self.cur.next
                self.cur_index += 1
        else:
            self.cur = self.head
            self.cur_index = 0
            while self.cur_index < rand_index:
                self.cur = self.cur.next
                self.cur_index += 1
        return self.cur.val
      
class Solution:
    '''reservoir sampling
    '''
    def __init__(self, head: Optional[ListNode]):
        self.head = head
    
    def getRandom(self) -> int:
        i = 0
        chosen_val = 0
        cur = self.head

        while cur:
            if random.randint(0, i) == 0:
                chosen_val = cur.val
            cur = cur.next
            i += 1

        return chosen_val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

