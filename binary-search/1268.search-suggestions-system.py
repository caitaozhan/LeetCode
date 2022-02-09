#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start

from bisect import bisect_left

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ans = []
        for i in range(1, len(searchWord) + 1):
            prefix = searchWord[0:i]
            insert_index = bisect_left(products, prefix)
            tmp = []
            for j in range(insert_index, min(insert_index+3, len(products))):
                if products[j][0:i] == prefix:
                    tmp.append(products[j])
                else:
                    break
            ans.append(tmp)
        return ans
        
# @lc code=end

