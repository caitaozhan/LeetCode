#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#

from collections import Counter
from heapq import heappush, heappop, nsmallest
from typing import List


class Node:
    def __init__(self, word, count):
        self.word = word
        self.count = count
    
    def __lt__(self, other):
        if self.count < other.count:
            return True
        if self.count == other.count and self.word > other.word:
            return True
        return False


# @lc code=start
class Solution:
    '''first use min heap to get the top k frequent words, O(nlogk)
       then do another sorting, O(klogk)
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        for word, count in counter.items():
            heappush(heap, Node(word, count)) # (ascend, descend)
            if len(heap) > k:
                heappop(heap)
        ans = sorted(heap, reverse=True)      # (descend, ascend)
        return [node.word for node in ans]


class Solution:
    '''nlargest: Heapify a max heap, then pop the top k elements
       but it is harder to reverse the order of a string comparing to integer
       so, let's use nsmallest...
       O(klogn)
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        return nsmallest(k, counter.keys(), key=lambda x: (-counter[x], x))

words = ["i","love","leetcode","i","love","coding"]
k = 2
s = Solution()
print(s.topKFrequent(words, k))
        

        
# @lc code=end

