#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

from collections import defaultdict

# @lc code=start
class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.timedata = defaultdict(list)
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station = self.checkin[id][0]
        checkin_time = self.checkin[id][1]
        self.timedata[(checkin_station, stationName)].append(t - checkin_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.timedata[(startStation, endStation)]
        return sum(times)/len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

