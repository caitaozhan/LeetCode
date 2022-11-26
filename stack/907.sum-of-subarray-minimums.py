#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

from typing import List

# @lc code=start
class Solution:
    '''two key points:
       1) count the contribution of each element. same idea is leetcode #828: Count Unique Characters of All Substrings of a Given String
       2) use an increasing monotone stack.
       I got both two key points right, but still failed to solve it. Because I didn't get the monotone stack correct
       So, we need to fill the two arrays left and right. The third key point is to 
       3) fill an element of left and right when it is poped out from the stack.
       My failed attempt is to fill an element of left and right when it is iterated in the for loop...
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # step 1: build the left and right array
        n = len(arr)
        left  = [-1] * n  # x=left[i] means it is the smallest item from [i-x+1] to [i]
        right = [-1] * n  # the x=right[i] means it is the single smallest item from [i] to [i+x-1]
        stack = []        # monotone (strict) increasing stack, index in the stack
        arr.append(-1)    # a small trick to pop out all the elements
        for i in range(n+1):
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                left[idx]  = idx - stack[-1] if stack else idx - (-1)
                right[idx] = i - idx
            stack.append(i)
        # step 2: get the answer
        ans = 0
        for i in range(n):
            ans += (left[i] * right[i]) * arr[i]
        MOD = 10**9 + 7
        return ans % MOD



class Solution:
    '''saves some space by not using a left and right array, and also a little faster
    '''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        stack = []        # monotone (strict) increasing stack, index in the stack
        arr.append(-1)    # a small trick to pop out all the elements
        for i in range(n+1):
            while stack and arr[i] <= arr[stack[-1]]:
                idx = stack.pop()
                left  = idx - stack[-1] if stack else idx - (-1)
                right = i - idx
                ans += (left * right) * arr[idx]
            stack.append(i)
        MOD = 10**9 + 7
        return ans % MOD


arr = [1,3,2,1,4,2]
# arr = [4,3,2,1]
s = Solution()
print(s.sumSubarrayMins(arr))


# @lc code=end

