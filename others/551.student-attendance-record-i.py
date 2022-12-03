#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#


# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for ch in s:
            if ch == 'P':
                late = 0
            elif ch == 'L':
                late += 1
                if late == 3:
                    return False
            else:
                late = 0
                absent += 1
                if absent == 2:
                    return False
        return True

        
# @lc code=end

