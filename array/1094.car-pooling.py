#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#
# https://leetcode.com/problems/car-pooling/description/
#
# algorithms
# Medium (56.60%)
# Likes:    859
# Dislikes: 34
# Total Accepted:    52.5K
# Total Submissions: 89.4K
# Testcase Example:  '[[2,1,5],[3,3,7]]\n4'
#
# You are driving a vehicle that has capacity empty seats initially available
# for passengers.  The vehicle only drives east (ie. it cannot turn around and
# drive west.)
# 
# Given a list of trips, trip[i] = [num_passengers, start_location,
# end_location] contains information about the i-th trip: the number of
# passengers that must be picked up, and the locations to pick them up and drop
# them off.  The locations are given as the number of kilometers due east from
# your vehicle's initial location.
# 
# Return true if and only if it is possible to pick up and drop off all
# passengers for all the given trips. 
# 
# 
# 
# Example 1:
# 
# 
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000
# 
# 
#

# @lc code=start
from itertools import accumulate
from typing import List

class Solution:
    '''This solution works if the start and end are integers.
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        person = [0 for _ in range(1001)]
        for num, start, end in trips:
            person[start] += num
            person[end] -= num
        maxx = max(accumulate(person))
        return True if maxx <= capacity else False


class Solution2:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from_list = sorted(trips, key = lambda x: x[1])
        to_list   = sorted(trips, key = lambda x: x[2])
        current = 0
        i, j = 0, 0    # i is for from_list, j is for to_list
        while i < len(from_list):
            if from_list[i][1] < to_list[j][2]:
                current += from_list[i][0]
                i += 1
            elif to_list[j][2] < from_list[i][1]:
                current -= to_list[j][0]
                j += 1
            else:      # from_list[i][1] == to_list[j][2]
                current += from_list[i][0]
                current -= to_list[j][0]
                i += 1
                j += 1

            if current > capacity:
                return False

        return True
# @lc code=end

