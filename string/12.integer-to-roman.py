#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        mydict = {
            1:    'I',
            4:    'IV',
            5:    'V',
            9:    'IX',
            10:   'X',
            40:   'XL',
            50:   'L',
            90:   'XC',
            100:  'C',
            400:  'CD',
            500:  'D',
            900:  'CM',
            1000: 'M'
        }

        ans = ''
        for key, val in sorted(mydict.items(), key=lambda x: x[0], reverse=True):
            if num < key:
                continue
            rep = num // key
            ans += val * rep
            num -= key * rep
        return ans
        

num = 1994
s = Solution()
print(s.intToRoman(num))

        
# @lc code=end

