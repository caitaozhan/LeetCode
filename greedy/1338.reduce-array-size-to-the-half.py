#
# @lc app=leetcode id=1338 lang=python3
#
# [1338] Reduce Array Size to The Half
#
# https://leetcode.com/problems/reduce-array-size-to-the-half/description/
#
# algorithms
# Medium (65.85%)
# Likes:    196
# Dislikes: 22
# Total Accepted:    17.7K
# Total Submissions: 26.8K
# Testcase Example:  '[3,3,3,3,5,5,5,2,2,7]'
#
# Given an array arr.  You can choose a set of integers and remove all the
# occurrences of these integers in the array.
# 
# Return the minimum size of the set so that at least half of the integers of
# the array are removed.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has
# size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array
# [3,3,3,3,5,5,5] which has size greater than half of the size of the old
# array.
# 
# 
# Example 2:
# 
# 
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the
# new array empty.
# 
# 
# Example 3:
# 
# 
# Input: arr = [1,9]
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: arr = [1000,1000,3,7]
# Output: 1
# 
# 
# Example 5:
# 
# 
# Input: arr = [1,2,3,4,5,6,7,8,9,10]
# Output: 5
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# arr.length is even.
# 1 <= arr[i] <= 10^5
# 
#


from typing import List
from collections import Counter

# 反证法：假设存在一个更优解，跟该算法得出的解比较一下，得出矛盾。我们假设一个否命题，导出一个矛盾。证明原命题是正确的。假设一个最优解。然后证明我的解不会比这个最优解差。

# 贪心：反证法，找反例，最后是凭感觉（最后的下策）
# 1. 尝试去证明做法的正确性。假设一个最优解，然后证明我的解不比他差。
# 2. 找反例。
# 3. 如果真的没有别的办法，在考场上就相信它是贪心。这是下下策。

# 看到”最“字，可以试试贪心。
# 用贪心可以先想想排序。


# @lc code=start
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans = 0
        summ = 0
        mycounter = Counter(arr)
        for val in sorted(mycounter.values(), reverse=True):
            summ += val
            ans += 1
            if summ >= len(arr)/2:
                break
        return ans



def test():
    x = [3,3,3,3,5,5,5,2,2,7]
    s = Solution()
    print(s.minSetSize(x))


if __name__ == '__main__':
    # test()
    pass

# @lc code=end

