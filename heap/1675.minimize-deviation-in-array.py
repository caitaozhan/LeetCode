#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

from typing import List
from heapq import heapify, heappush, heappop

# @lc code=start
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # record a number's upper bound
        upbound = []
        for num in nums:
            if num % 2 == 0:
                upbound.append(num)
            else:
                upbound.append(num * 2)

        # decrease all the even number to the smallest odd number
        maxx = 0
        nums_upbound = []
        for i in range(len(nums)):
            num = nums[i]
            while num % 2 == 0:
                num //= 2
            maxx = max(maxx, num)
            nums_upbound.append((num, upbound[i]))

        # now we can only increase number, increase the smallest number each time
        heapify(nums_upbound)
        minn = float('inf')
        while True:
            deviation = maxx - nums_upbound[0][0]
            minn = min(minn, deviation)
            item = heappop(nums_upbound)
            num, up = item[0], item[1]
            if 2 * num <= up:
                heappush(nums_upbound, (2 * num, up))
                maxx = max(maxx, 2 * num)
            else:
                break

        return minn
            


if __name__ == '__main__':
    # nums = [21, 23, 22, 26, 28, 38, 44, 46]
    nums = [1,2,3,4,5,6]
    nums = [1,2,3,4]
    nums = [4,1,5,20,3]
    # nums = [4,22,26,30]
    # nums = [3, 5]
    # nums = [11, 16, 19]
    # nums = [4, 8, 16]
    # nums = [1,3,5,7]

    s = Solution()
    print(s.minimumDeviation(nums))
    


# @lc code=end

