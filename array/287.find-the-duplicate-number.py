#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset = set()
        for num in nums:
            if num in myset:
                return num
            myset.add(num)

class Solution:
    '''this solution is based on the special condition of the input array: 
       size n + 1 and the elements are 1 to n integers
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num)
            if nums[index] < 0:
                return index
            nums[index] = -nums[index]

class Solution:
    '''this solution is based on a faster pointer and slow pointer
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        # step 1: find the location where the slow and fast meet
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # step 2: the fast's speed reduce to slow's speed. reset slow to beginning. wait until they meet again
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow



# @lc code=end

