#
# @lc app=leetcode id=2034 lang=python3
#
# [2034] Stock Price Fluctuation 
#


class Node:
    def __init__(self, time, value):
        self.time = time
        self.value = value

class Heap:
    '''min heap'''
    def __init__(self):
        self.array = []
        self.time2idx = {}

    def parent_idx(self, cur: int) -> int:
        if cur == 0:
            return -1
        return int((cur - 1) / 2)

    def swap(self, cur_idx: int, parent_idx: int):
        '''first update the self.time2idx mapping, then update the self.array
        '''
        parent_time = self.array[parent_idx].time
        cur_time    = self.array[cur_idx].time
        self.time2idx[parent_time] = cur_idx
        self.time2idx[cur_time]    = parent_idx
        self.array[cur_idx], self.array[parent_idx] = self.array[parent_idx], self.array[cur_idx]

    def insert(self, time, value):
        '''put the key at the end of the array, then move up as much as needed'''
        cur = len(self.array)
        self.time2idx[time] = cur
        self.array.append(Node(time, value))
        parent = self.parent_idx(cur)
        while parent >= 0:
            if self.array[cur].value < self.array[parent].value:
                self.swap(cur, parent)
                cur = parent
                parent = self.parent_idx(cur)
            else:
                break

    def update(self, time, value):
        idx = self.time2idx[time]
        old_value = self.array[idx].value
        self.array[idx].value = value
        if value < old_value:   # move up
            cur = idx
            parent = self.parent_idx(cur)
            while parent >= 0:
                if self.array[cur].value < self.array[parent].value:
                    self.swap(cur, parent)
                    cur = parent
                    parent = self.parent_idx(cur)
                else:
                    break
        elif value > old_value: # move down
            cur = idx
            while True:
                smallest = cur
                left_child_idx  = 2 * cur + 1
                right_child_idx = 2 * cur + 2
                if left_child_idx < len(self.array) and self.array[left_child_idx].value < self.array[smallest].value:
                    smallest = left_child_idx
                if right_child_idx < len(self.array) and self.array[right_child_idx].value < self.array[smallest].value:
                    smallest = right_child_idx
                if smallest != cur:
                    self.swap(cur, smallest)
                    cur = smallest
                else:
                    break
        else:  # don't move
            pass

    def getmin(self) -> int:
        return self.array[0].value



# @lc code=start
class StockPrice:

    def __init__(self):
        self.minheap = Heap()
        self.maxheap = Heap()
        self.latest_node = Node(-1, 0)

    def update(self, timestamp: int, price: int) -> None:
        # update current
        if timestamp > self.latest_node.time:
            self.latest_node = Node(timestamp, price)
        elif timestamp == self.latest_node.time:
            self.latest_node.value = price
        else:
            pass
        # update the heap
        if timestamp in self.minheap.time2idx:
            self.minheap.update(timestamp, price)
            self.maxheap.update(timestamp, -price)
        else:
            self.minheap.insert(timestamp, price)
            self.maxheap.insert(timestamp, -price)

    def current(self) -> int:
        return self.latest_node.value

    def maximum(self) -> int:
        return -self.maxheap.getmin()

    def minimum(self) -> int:
        return self.minheap.getmin()


# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(1, 2)
obj.update(2, 3)
obj.update(3, 1)
print(obj.minimum())
obj.update(1, 0)
print(obj.minimum())
obj.update(4, 5)
obj.update(1, 8)
print(obj.minimum())

# param_2 = obj.current()
# param_3 = obj.maximum()
# @lc code=end

