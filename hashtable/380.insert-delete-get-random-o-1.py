#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

import random

# @lc code=start
class RandomizedSet:
    '''constant time insert/delete --> set
       constant time random access --> array
       so need a hybrid set-array
    '''
    def __init__(self):
        self.array = []
        self.next = 0      # the next pointer is the index right after the last element
        self.val2idx = {}

    def insert(self, val: int) -> bool:
        '''either insert val at the end of the array, or in the middle
        '''
        if val not in self.val2idx:
            if self.next == len(self.array):
                self.array.append(val)
            else:
                self.array[self.next] = val
            self.val2idx[val] = self.next
            self.next += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        '''replace the val by the last element in the array
        '''
        if val in self.val2idx:
            idx = self.val2idx[val]
            if idx == self.next - 1:      # val happen to be the last element in the array
                self.next -= 1
                del self.val2idx[val]
            else:                         # val is in the middle of the array
                last_element = self.array[self.next - 1]
                self.array[idx] = last_element
                del self.val2idx[val]
                self.val2idx[last_element] = idx
                self.next -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        idx = random.randint(0, self.next - 1)
        return self.array[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

