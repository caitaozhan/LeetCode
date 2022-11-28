'''
You have information about n different recipes. 
You are given a string array recipes and a 2D string array ingredients. 
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
Ingredients to a recipe may need to be created from other recipes, 
i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, 
and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
'''

from typing import List
from collections import defaultdict


class Solution:
    '''topological sort based method
    '''
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        g = defaultdict(list)
        indegree = {recipe: 0 for recipe in recipes}
        for recipe, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                g[ingredient].append(recipe)
                indegree[recipe] += 1
        queue = supplies.copy()
        ans = []
        while queue:
            new_queue = []
            for node in queue:
                for nxt in g[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        ans.append(nxt)
                        new_queue.append(nxt)
            queue = new_queue
        return ans


recipes = ["bread"]
ingredients = [["yeast","flour"]]
supplies = ["yeast","flour","corn"]

# recipes = ["ju","fzjnm","x","e","zpmcz","h","q"]
# ingredients = [["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]]
# supplies = ["f","hveml","cpivl","d"]

s = Solution()
print(s.findAllRecipes(recipes, ingredients, supplies))
