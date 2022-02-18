#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
class Solution:
    '''monotone increase stack, putting index in the stack, and explicitly removing the k digit in the end'''
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remove = []
        for i in range(len(num)):
            while stack and num[i] < num[stack[-1]] and len(remove) < k:
                index = stack.pop()
                remove.append(index)    
            stack.append(i)
            if len(remove) == k:
                    break

        if k > len(remove):
            remove.extend(stack[::-1][:k - len(remove)])
        remove = set(remove)
        
        ans = []
        count = 0
        for i, char in enumerate(num):
            if count < k and i in remove:
                count += 1
                continue
            ans.append(char)

        if ans:
            return str(int(''.join(ans)))
        else:
            return '0'


class Solution:
    '''monotone increase stack, putting the real digit in the queue, and keeping it as the remaining ones. (faster than the previous one)'''
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k > 0 and stack and i < stack[-1]:
                stack.pop()
                k -= 1  
            stack.append(i)  

        while k > 0:
            stack.pop()
            k -= 1

        ans = ''.join(stack)
        return str(int(''.join(ans))) if ans != '' else '0'


if __name__ == '__main__':
    s = Solution()
    num = "1432219"
    k = 3

    # num = '10200'
    # k = 1

    num = '53100131'
    k = 8

    num = '10'
    k = 2

    num = "93128749200009"
    k = 6
    print(s.removeKdigits(num, k))

# @lc code=end

