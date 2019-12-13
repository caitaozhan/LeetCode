#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (28.64%)
# Likes:    4123
# Dislikes: 172
# Total Accepted:    398.1K
# Total Submissions: 1.4M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
class LRUCache:
    '''OrderedDict is the best data structure for this.
       fail-1
    '''

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.capacity = capacity
        self.lru_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru_dict:
            val = self.lru_dict.pop(key)  # delete and reinsert
            self.lru_dict[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru_dict:   # fail-1: if already exist the key, just do an update: self.lru_dict[key] = value
            self.lru_dict.pop(key) # fail-2: my fix for fail-1 is not correct, it should be delete and reinsert
            self.lru_dict[key] = value
        else:
            if len(self.lru_dict) < self.capacity:
                self.lru_dict[key] = value
            else:
                self.lru_dict.popitem(last=False)
                self.lru_dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

