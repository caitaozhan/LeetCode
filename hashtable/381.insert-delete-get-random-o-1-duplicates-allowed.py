#
# @lc app=leetcode id=381 lang=python3
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

import random
from collections import defaultdict

# @lc code=start
class RandomizedCollection:
    '''a more difficult version of leetcode #381
       the key is to "upgrade" the built-in dict used in #381 to defaultdict(set) in this problem
    '''
    def __init__(self):
        self.mydict = defaultdict(set)
        self.array = []

    def insert(self, val: int) -> bool:
        ret = False
        if len(self.mydict[val]) == 0:
            ret = True
        self.mydict[val].add(len(self.array))  # val's index is right after the last index
        self.array.append(val)
        return ret

    def remove(self, val: int) -> bool:
        if len(self.mydict[val]) == 0:
            return False
        last_idx = len(self.array) - 1
        if last_idx in self.mydict[val]:   # val is at the last element
            self.mydict[val].remove(last_idx)
        else:                              # val is not at the last element
            idx_remove = self.mydict[val].pop()  # a random element in the set
            last_element = self.array[last_idx]
            self.array[idx_remove] = last_element
            self.mydict[last_element].remove(last_idx)
            self.mydict[last_element].add(idx_remove)
        self.array.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.array) - 1)
        return self.array[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

