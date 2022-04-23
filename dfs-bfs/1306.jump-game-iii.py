#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

from typing import List

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        target = set([i for i in range(len(arr)) if arr[i] == 0])
        visited = [0] * len(arr)
        can_reach = False

        def dfs(cur):
            nonlocal can_reach
            if can_reach is True:
                return
            if cur in target:
                can_reach = True
                return
            visited[cur] = 1
            step = arr[cur]
            nxt1 = cur + step
            nxt2 = cur - step
            if 0 <= nxt1 < len(arr) and visited[nxt1] == 0:
                dfs(nxt1)
            if 0 <= nxt2 < len(arr) and visited[nxt2] == 0:
                dfs(nxt2)
            visited[cur] = 0

        dfs(start)
        return can_reach

arr = [4,2,3,0,3,1,2]
start = 5
s = Solution()
print(s.canReach(arr, start))
        

        
# @lc code=end

