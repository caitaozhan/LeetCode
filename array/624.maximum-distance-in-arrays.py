'''

Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].


'''

from typing import List

class Solution:
    ''' idea 1: only consider the min and max of each array
        idea 2: do a sorting based on min and max, there are three cases to consider.
    '''
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays2 = []
        for i, arr in enumerate(arrays):
            arrays2.append((i, min(arr), max(arr)))
        min_increase = sorted(arrays2, key=lambda x:x[1])
        max_decrease = sorted(arrays2, key=lambda x:x[2], reverse=True)
        if min_increase[0][0] != max_decrease[0][0]:
            return max_decrease[0][2] - min_increase[0][1]
        else:
            candi1 = max_decrease[0][2] - min_increase[1][1]
            candi2 = max_decrease[1][2] - min_increase[0][1]
            return max(candi1, candi2)
        