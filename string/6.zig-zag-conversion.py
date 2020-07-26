#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (35.74%)
# Likes:    1710
# Dislikes: 4679
# Total Accepted:    466.8K
# Total Submissions: 1.3M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        series = []
        d = 2 * numRows - 2
        for i in range(numRows):
            tmp = i
            row = []
            while tmp < len(s):
                row.append(tmp)
                tmp += d
            series.append(row)
        
        ans = []

        # step 1: first row
        for indx in series[0]:
            ans.append(s[indx])

        # step 2: second row to numRows-1 row
        for i in range(1, numRows-1):
            j = 0
            while True:
                indx = series[i][j] if j < len(series[i]) else float('inf')
                if indx >= len(s):
                    break
                ans.append(s[indx])
                indx = series[-1][j] + (numRows - 1 - i) if j < len(series[-1]) else float('inf')
                if indx >= len(s):
                    break
                ans.append(s[indx])
                j += 1

        # step 3: last row  NOTE: what if there is less than three rows?
        for indx in series[-1]:
            ans.append(s[indx])

        return ''.join(ans)

# @lc code=end

