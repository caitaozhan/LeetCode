'''

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".


Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

'''

class Count:
    def __init__(self, char, count):
        self.char = char
        self.count = count
    
    def __lt__(self, other):
        return self.count > other.count
    
    def __str__(self):
        return '{}-{}'.format(self.char, self.count)


class Solution:
    '''Greedy solution
    '''
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mylist = [Count('a', a), Count('b', b), Count('c', c)]
        ans = []
		
		# step 1: add two same charecters at once
        while True:
            mylist.sort()
            last = ans[-1] if len(ans) > 0 else None
            if mylist[0].count >= 2:
                if mylist[1].count >= 1: 
                    if last != mylist[0].char:          # 'aab'
                        ans.append(mylist[0].char)
                        ans.append(mylist[0].char)
                        ans.append(mylist[1].char)
                    else:
                        ans.append(mylist[1].char)      # 'baa'
                        ans.append(mylist[0].char)
                        ans.append(mylist[0].char)
                    mylist[0].count -= 2
                    mylist[1].count -= 1
                else:
                    if last != mylist[0].char:
                        ans.append(mylist[0].char)      # 'aa'
                        ans.append(mylist[0].char)
                        mylist[0].count -= 2
                    else:
                        break
            else:
                break

		# step 2: cannot add two same charecters at once
        mylist.sort()
        last = ans[-2] + ans[-1] if len(ans) >= 2 else None
        if last == mylist[0].char * 2:
            append = False
            for i in [1, 2]:
                if mylist[i].count == 1:
                    ans.append(mylist[i].char)
                    append = True
            if append:
                ans.append(mylist[0].char)
        else:
            for i in [0, 1, 2]:
                if mylist[i].count == 1:
                    ans.append(mylist[i].char)

        return ''.join(ans)


def test1():
    s = Solution()
    print(s.longestDiverseString(7, 1, 0))

if __name__ == '__main__':
    test1()
