class Solution:
    ''' greedy approach. start from the left side, and everytime pick the smallest number on the right side that is able to swap, then do the swap
    '''
    def minInteger(self, num: str, k: int) -> str:
        min_num = sorted(list(num))
        min_num = ''.join(min_num)
        i = 0
        to_find = 0
        while num != min_num and k > 0 and i < len(num):
            indx = num.find(str(to_find), i)
            while indx != -1:
                if indx - i <= k:   # able to swap
                    num = num[:i] + num[indx] + num[i:indx] + num[indx+1:]
                    k -= (indx - i)
                    i += 1
                    to_find = 0
                    indx = num.find(str(to_find), i)
                else:
                    break
            to_find = (to_find + 1) % 10
        return num

def test():
    num = "294984148179"
    k = 11

    s = Solution()
    print(s.minInteger(num, k))

test()
