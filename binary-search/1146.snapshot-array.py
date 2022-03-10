#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

from collections import defaultdict

# @lc code=start
class SnapshotArray3:
    '''naive implementation
       the time complexity of self.set() is O(1) 
       the time complexity of self.snap() is O(length) 
       the time complexity of self.snapshot() is O(1)
    '''
    def __init__(self, length: int):
        self.array = [0] * length
        self.snapshot = []
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index] = val

    def snap(self) -> int:
        self.snapshot.append(self.array[:])
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id][index]


class SnapshotArray2:
    '''
       time complexity of self.set() is O(1)
       time complexity of self.snap() is O(1)
       time complexity of self.get() is O(log snap_id)
    '''
    def __init__(self, length: int):
        self.length = length
        self.snapshot = defaultdict(list)  # an element of list is (snap_id, val)
        self.snap_id = 0
        for i in range(self.length):
            self.snapshot[i].append((self.snap_id, 0))
    
    def set(self, index: int, val: int) -> None:
        self.snapshot[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshot_list = self.snapshot[index]
        return self.binary_search(snapshot_list, snap_id)
    
    def binary_search(self, snapshot_list, snap_id):
        '''an element of snapshot_list is (snap_id, val), snap_id is ordered
           there might be duplicates
        '''
        low = 0
        high = len(snapshot_list)
        while low < high:
            mid = (low + high) // 2
            if snapshot_list[mid][0] <= snap_id:
                low = mid + 1
            else:
                high = mid
        
        return snapshot_list[low-1][1]


class SnapshotArray:
    '''
       time complexity of self.set() is O(1)
       time complexity of self.snap() is O(1)
       time complexity of self.get() is O(log snap_id)
    '''
    def __init__(self, length: int):
        self.length = length
        self.snapshot = defaultdict(list)  # an element of list is (snap_id, val)
        self.snap_id = 0
        for i in range(self.length):
            self.snapshot[i].append((self.snap_id, 0))

    def set(self, index: int, val: int) -> None:
        ''' NOTE: do not need to append every time, save memory, and also time
        '''
        last = self.snapshot[index][-1]
        if last[0] == self.snap_id:
            self.snapshot[index][-1] = (self.snap_id, val)
        else:
            self.snapshot[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapshot_list = self.snapshot[index]
        return self.binary_search(snapshot_list, snap_id)
    
    def binary_search(self, snapshot_list, snap_id):
        '''an element of snapshot_list is (snap_id, val), snap_id is ordered
           there are NO duplicates
        '''
        low = 0
        high = len(snapshot_list)
        while low < high:
            mid = (low + high) // 2
            if snapshot_list[mid][0] < snap_id:
                low = mid + 1
            elif snapshot_list[mid][0] > snap_id:
                high = mid
            else:
                return snapshot_list[mid][1]
        
        return snapshot_list[low-1][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

