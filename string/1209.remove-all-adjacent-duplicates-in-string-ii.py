'''
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters 
from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

'''

class Solution:
    '''naive O(n^2) simulation based solution
    '''
    def removeDuplicates(self, s: str, k: int) -> str:
        def removehelper(s: list, k: int):
            '''return True if there are some duplicates actually removed, else False
            '''
            remove = False
            new_s = []
            i = 0
            j = 1
            dup = 0
            while j < len(s):
                if s[j] == s[j - 1]:
                    dup += 1
                    if dup == k - 1:
                        remove = True
                        i = j + 1
                        j += 2
                    else:
                        j += 1
                else:
                    dup = 0
                    while i < j:
                        new_s.append(s[i])
                        i += 1
                    j += 1
            while i < len(s):
                new_s.append(s[i])
                i += 1

            return remove, new_s

        s = list(s)
        remove = True
        while remove:
            remove, s = removehelper(s, k)
        
        return ''.join(s)


class Solution:
    '''using a stack, O(n)
    '''
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if not stack:
                stack.append([c, 1])
            else:
                if c == stack[-1][0]:
                    count = stack[-1][1]
                    if count < k - 1:
                        stack[-1][1] += 1
                    else:
                        stack.pop()
                else:
                    stack.append([c, 1])
    
        ans = []
        for c, repeat in stack:
            ans.extend([c]*repeat)
        return ''.join(ans)



string = "deeedbbcccbdaa"
# string = 'deeedbbcccbdaa'
k = 3

s = Solution()
print(s.removeDuplicates(string, k))
