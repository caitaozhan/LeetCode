#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    '''backtrack / brute force, O(n*n!) TLE
    '''
    def __init__(self):
        self.counter = 0
        self.ans = None

    def getPermutation(self, n: int, k: int) -> str:

        def dfs(stack, visited):
            if self.ans:
                return
            if len(stack) == n:
                self.counter += 1
                if self.counter == k:
                    self.ans = ''.join(map(str,stack))
            
            for i in range(1, n + 1):
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(i)
                    dfs(stack, visited)
                    stack.pop()
                    visited[i] = 0

        visited = [0] * (n + 1)
        dfs(stack=[], visited=visited)
        return self.ans


class Solution:
    '''analytical method, O(n^2)
    '''
    def factorial(self, n):
        prod = 1
        for i in range(1, n + 1):
            prod *= i
        return prod

    def getPermutation(self, n: int, k: int) -> str:
        factorial = [self.factorial(i) for i in range(n + 1)]
        nums = [i for i in range(1, n + 1)]
        ans = []
        counter = 0
        while len(ans) != n:
            for i in nums:
                tmp = factorial[n - len(ans) - 1]
                if counter + tmp >= k:
                    ans.append(i)
                    nums.remove(i)
                    break
                counter += tmp

        return ''.join(map(str, ans))



n = 9
k = 305645
# ans = 856412937
s = Solution()
print(s.getPermutation(n, k))

# @lc code=end

