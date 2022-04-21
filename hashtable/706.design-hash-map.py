#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.prime = 20011
        self.array = [[] for _ in range(self.prime)]

    def _hash(self, key):
        return key % self.prime

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        for i in range(len(self.array[index])):
            k = self.array[index][i][0]
            if k == key:
                self.array[index][i][1] = value
                return
        self.array[index].append([key ,value])

    def get(self, key: int) -> int:
        index = self._hash(key)
        for i in range(len(self.array[index])):
            k = self.array[index][i][0]
            if k == key:
                return self.array[index][i][1]
        return -1

    def remove(self, key: int) -> None:
        index = self._hash(key)
        for i in range(len(self.array[index])):
            k = self.array[index][i][0]
            if k == key:
                v = self.array[index][i][1]
                self.array[index].remove([k, v])
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

