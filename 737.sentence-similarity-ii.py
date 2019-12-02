'''

Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

'''

from typing import List

class Solution:
    '''build a graph and do DSF
    '''
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in pairs:    # build graph
            graph[u].append(v)
            graph[v].append(u)

        for word1, word2 in zip(words1, words2):
            visited = {word1}  # mark as visited
            stack   = [word1]  # put in stack
            while stack:
                cur = stack.pop()
                if cur == word2:  # found --> it is similar
                    break
                for nxt in graph[cur]:
                    if nxt not in visited:
                        visited.add(nxt)
                        stack.append(nxt)
            else:
                return False
        return True


def test():
    print()
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]

    s = Solution()
    print(s.areSentencesSimilarTwo(words1, words2, pairs))


def test2():
    print()
    words1 = ["great", "acting", "skillss"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]

    s = Solution()
    print(s.areSentencesSimilarTwo(words1, words2, pairs))

if __name__ == '__main__':
    test()
    test2()
