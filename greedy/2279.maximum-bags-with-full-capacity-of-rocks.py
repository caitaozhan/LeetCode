'''

You have n bags numbered from 0 to n - 1. You are given two 0-indexed integer arrays capacity and rocks. 
The ith bag can hold a maximum of capacity[i] rocks and currently contains rocks[i] rocks. 
You are also given an integer additionalRocks, the number of additional rocks you can place in any of the bags.

Return the maximum number of bags that could have full capacity after placing the additional rocks in some bags.

'''

class Solution:
    '''greedy: smallest capacity left first
    '''
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [cap - rock for cap, rock in zip(capacity, rocks)]
        diff.sort()
        ans = 0
        for d in diff:
            if additionalRocks >= d:
                additionalRocks -= d
                ans += 1
            else:
                break
        return ans
