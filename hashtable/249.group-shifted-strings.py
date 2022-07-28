'''

[249] group shifted strings

We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

'''

from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for s in strings:
            base = s[0]
            key = [0]
            for i in range(1, len(s)):
                key.append((ord(s[i]) - ord(base)) % 26)
            mydict[tuple(key)].append(s)
        return list(mydict.values())