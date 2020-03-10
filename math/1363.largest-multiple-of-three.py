'''
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

Input: digits = [8,1,9]
Output: "981"

Input: digits = [8,6,7,1,0]
Output: "8760"

Input: digits = [1]
Output: ""

Input: digits = [0,0,0,0,0,0]
Output: "0"

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.

'''

from typing import List

class Solution:

    def list2str(self, digits):
        if len(digits) == 0:
            return ''
        elif digits[0] == 0:
            return '0'
        else:
            return ''.join(map(str, digits))

    def remove(self, digits, remainder_one, remainder_two):
        '''From a list of sorted digits (high --> low), remove remainder_one number of digits whose
        remainder is one, or remove remainder_two number of digits whose remainder is two.
        '''
        total = remainder_one + remainder_two
        new = []
        for i in range(len(digits)-1, -1, -1):
            if remainder_one and digits[i]%3 == 1:
                remainder_one -= 1
                continue
            elif remainder_two and digits[i]%3 == 2:
                remainder_two -= 1
                continue
            new.append(digits[i])
        if len(digits) - len(new) == total:
            new.reverse()
            return new
        else:
            return []

    def choose_one(self, digits1, digits2):
        str1 = self.list2str(digits1)
        str2 = self.list2str(digits2)
        if len(str1) > len(str2):
            return str1
        elif len(str1) < len(str2):
            return str2
        else:
            if str1 > str2:
                return str1
            else:
                return str2

    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        summation = sum(digits)
        remainder = summation % 3
        ans = ''
        if remainder == 0:
            ans = self.list2str(digits)
        elif remainder == 1:
            digits1 = self.remove(digits, 1, 0)
            digits2 = self.remove(digits, 0, 2)
            ans = self.choose_one(digits1, digits2)
        else:                      # remainder == 2
            digits1 = self.remove(digits, 0, 1)
            digits2 = self.remove(digits, 2, 0)
            ans = self.choose_one(digits1, digits2)
        return ans
