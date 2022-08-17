#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        vals = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        keys = [chr(ord('a')+i) for i in range(26)]
        morse = {}
        for key, val in zip(keys, vals):
            morse[key] = val
        transformation = set()
        for word in words:
            tmp = []
            for ch in word:
                tmp.append(morse[ch])
            transformation.add(''.join(tmp))
        return len(transformation)



# @lc code=end

