#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

from typing import List

# @lc code=start
class Solution:
    '''dfs'''
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0] * len(arr)

        def dfs(cur):
            if 0 <= cur < len(arr) and visited[cur] == 0:
                if arr[cur] == 0:
                    return True
                visited[cur] = 1   # do not need to mark back to 0, every node just need to visit once.
                step = arr[cur]
                nxt1 = cur + step
                nxt2 = cur - step
                return dfs(nxt1) or dfs(nxt2)

        return dfs(start)



from collections import deque

class Solution:
    '''bfs'''
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [0] * len(arr)
        queue = deque()
        queue.append(start)
        while queue:
            cur = queue.popleft()
            visited[cur] = 1
            if arr[cur] == 0:
                return True
            nxt1 = cur + arr[cur]
            nxt2 = cur - arr[cur]
            if 0 <= nxt1 < len(arr) and visited[nxt1] == 0:
                queue.append(nxt1)
            if 0 <= nxt2 < len(arr) and visited[nxt2] == 0:
                queue.append(nxt2)
            
        return False





arr = [4,2,3,0,3,1,2]
start = 5
s = Solution()
print(s.canReach(arr, start))

# @lc code=end
