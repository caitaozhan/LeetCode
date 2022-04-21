#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.prime = 20011
        self.array = [[] for _ in range(self.prime)]  # a better method is to use a linked list

    def _hash(self, key):
        return key % self.prime

    def add(self, key: int) -> None:
        index = self._hash(key)
        for item in self.array[index]:
            if item == key:
                return
        self.array[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        try:
            self.array[index].remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        for item in self.array[index]:
            if item == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

