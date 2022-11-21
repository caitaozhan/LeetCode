#
# @lc app=leetcode id=359 lang=python3
#
# [359] Logger Rate Limiter
#


class Logger:

    def __init__(self):
        self.records = {}  # message -> timestamp

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.records:
            prev_time = self.records[message]
            if timestamp - prev_time < 10:
                return False
            else:
                self.records[message] = timestamp
                return True
        else:
            self.records[message] = timestamp
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


