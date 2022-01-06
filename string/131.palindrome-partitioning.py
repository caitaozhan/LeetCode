#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

from typing import List


# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # step 1: do a DP to find out all the palindromes
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        # initialize single character string
        for i in range(size):
            dp[i][i] = 1
        # initialize double character string
        for i in range(size-1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
        # fill up the rest of the dp array
        for length in range(2, size):
            for i in range(size - length):
                for j in range(i + length, size):
                    if dp[i+1][j-1] == 1 and s[i] == s[j]:
                        dp[i][j] = 1
        
        # for row in dp:
        #     print(row)

        def dfs(s, start, end, dp, cur, sol):
            cur.append(start)
            if start == end:
                sol.append(cur[:])
                return
            if start > end + 1:
                raise('error')

            dp_row = dp[start]
            for j in range(len(dp_row)):
                if dp_row[j] == 1:
                    dfs(s, j + 1, end, dp, cur, sol)
                    cur.pop()

        # step 2: do a DFS to find all the partitions
        sol = []
        cur = []
        dfs(s, 0, size, dp, cur, sol)

        # step 3: generate the outputs
        ans = []
        for part in sol:
            tmp = []
            for i in range(len(part) - 1):
                tmp.append(s[part[i]:part[i + 1]])
            ans.append(tmp)

        return ans


if __name__ == "__main__":
    s = Solution()
    # s.partition('ababaab')
    # print(s.partition('aab'))
    # print(s.partition('a'))
    print(s.partition('cbbbcc'))

# @lc code=end

