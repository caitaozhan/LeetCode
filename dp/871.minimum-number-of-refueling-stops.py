#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

from email.policy import default
from typing import List

# @lc code=start
class Solution:
    '''subproblem: dp[i][j] is the max fuel left when reaching ith station with stopping j # of stations in between
       a O(n^3) solution with many pruning that finally barely passed...
    '''
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        def dist(j: int, i: int) -> int:
            '''the distance from station j to i (j < i)
            '''
            return stations[i][0] - stations[j][0]

        def station_fuel(k: int) -> int:
            '''the fuel at station k
            '''
            return stations[k][1]

        upperbound = float('inf')
        stations.append([target, 0])
        n = len(stations)
        dp = [[float('-inf') for _ in range(n)] for _ in range(n)]  # -inf indicates cannot reach
        # initialization -- reaching ith station with 0 stopping
        for i in range(n):
            if startFuel - stations[i][0] >= 0:
                dp[i][0] = startFuel - stations[i][0]
        # solve the subproblems
        for i in range(1, n):
            for j in range(1, i + 1):
                if j > upperbound:
                    break
                for k in reversed(range(j-1, i)):
                    if dp[k][j] < 0 and dp[k][j-1] < 0:
                        break
                    fuel = max(dp[k][j] - (stations[i][0] - stations[k][0]),                       # no stopping at k
                               dp[k][j-1] + stations[k][1] - ((stations[i][0] - stations[k][0])))   # stopping at k
                    if fuel >= 0:
                        dp[i][j] = max(dp[i][j], fuel)
                        break
            for j in range(i + 1):
                if dp[i][j] >= (target - stations[i][0]):
                    upperbound = min(upperbound, j)
        # getting the answer
        for j in range(n):
            if dp[n-1][j] >= 0:
                return j
        return -1

from collections import defaultdict

class Solution:
    '''subproblem: dp[stops] is the max fuel left when reaching ith station with stopping stops # of stations before reaching ith station
                             where i is the iteration number
       almost O(n) solution
    '''
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        def dist(j: int, i: int) -> int:
            '''the distance from station j to i (j < i)
            '''
            return stations[i][0] - stations[j][0]

        def station_fuel(k: int) -> int:
            '''the fuel at station k
            '''
            return stations[k][1]

        stations.append([target, 0])
        n = len(stations)
        dp = defaultdict(lambda: float('-inf'))  # dp[stops] -> fuel, when reaching the ith station, taking 'stops', we have a max 'fuel'
        dp[0] = startFuel - stations[0][0]
        if dp[0] < 0:
            return -1
        upperbound = float('inf')
        for i in range(1, n):   # at the ith station, consider the subproblems at (i-1)th stations
            new_dp = defaultdict(lambda: float('-inf'))
            for subprob in dp.items():
                stops, fuel = subprob
                if stops > upperbound:
                    continue
                # stop at the (i-1)th station
                new_fuel = fuel + station_fuel(i-1) - dist(i-1, i)
                if new_fuel >= 0:
                    new_dp[stops+1] = max(new_dp[stops+1], new_fuel)  
                # no stop at the (i-1)th station
                new_fuel = fuel - dist(i-1, i)
                if new_fuel >= 0:
                    new_dp[stops] = max(new_dp[stops], new_fuel)
            dp = new_dp
            if len(dp) == 0:
                return -1
            for subprob in sorted(dp.items()):
                stops, fuel = subprob
                if fuel >= target - stations[i][0]:
                    upperbound = min(upperbound, stops)

        return min(dp.keys()) if len(dp) > 0 else -1



target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]

target = 100
startFuel = 10
stations = [[10,60],[20,20],[30,10]]

s = Solution()
print(s.minRefuelStops(target, startFuel, stations))


# @lc code=end

