#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

from typing import List

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # step 1: first the largest two elements
            if stones[0] >= stones[1]:
                first = stones[0]
                second = stones[1]
                first_index = 0
                second_index = 1
            else:
                first = stones[1]
                second = stones[0]
                first_index = 1
                second_index = 0
            for i in range(2, len(stones)):
                if stones[i] > first:
                    second = first
                    second_index = first_index
                    first = stones[i]
                    first_index = i
                elif stones[i] > second:
                    second = stones[i]
                    second_index = i
            # step 2: cancel the two stones
            if first == second:
                if first_index < second_index:
                    stones.pop(second_index)
                    stones.pop(first_index)
                else:
                    stones.pop(first_index)
                    stones.pop(second_index)
            else:
                stones[first_index] -= stones[second_index]
                stones.pop(second_index)
        
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

class Solution:
    '''a shorter solution that circumvent finding the largest two stones
    '''
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_largest(stones):
            index = stones.index(max(stones))
            stones[index], stones[-1] = stones[-1], stones[index]
            return stones.pop()

        while len(stones) > 1:
            s1 = remove_largest(stones)
            s2 = remove_largest(stones)
            if s1 > s2:
                stones.append(s1 - s2)
        
        return stones[0] if stones else 0


stones = [7,5,6,9,10,5]
s = Solution()
print(s.lastStoneWeight(stones))

# @lc code=end

