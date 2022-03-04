from collections import deque



class Solution802:
    # 802. Find Eventual Safe States
    # https://leetcode.com/problems/find-eventual-safe-states/
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adjlist = {i: [] for i in range(len(graph))}
        indegrees = {i: 0 for i in range(len(graph))}
        # bucket sort to return the result in ascending order
        safe = [False for i in range(len(graph))]
        for index, contents in enumerate(graph):
            for node in contents:
                adjlist[node].append(index)
                indegrees[index] += 1
        
        queue = deque([i for i in indegrees if indegrees[i] == 0])
        
        while queue:
            curr = queue.popleft()
            safe[curr] = True
            
            for neighbor in adjlist[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        
        ans = []
        for index, result in enumerate(safe):
            if result:
                ans.append(index)
        
        return ans

class Solution2115:
    # 2115. Find All Possible Recipes from Given Supplies
    # https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adjlist, indegrees = self.get_adjlist_and_indegrees(recipes, ingredients)
        queue = deque([i for i in indegrees if indegrees[i] == 0])
        answers = []
        supplies = set(supplies)
        
        while queue:
            curr_index = queue.popleft()
            if set(ingredients[curr_index]).issubset(supplies):
                answers.append(recipes[curr_index])
                supplies.add(recipes[curr_index])
            
            for next_index in adjlist[curr_index]:
                indegrees[next_index] -= 1
                if indegrees[next_index] == 0:
                    queue.append(next_index)
        
        return answers

    
    def get_adjlist_and_indegrees(self, recipes, ingredients):
        adjlist = {i: [] for i in range(len(recipes))}
        indegrees = {i: 0 for i in range(len(recipes))}
        recipe_to_index = {value: index for index, value in enumerate(recipes)}
        
        for index, contents in enumerate(ingredients):
            for ingredient in contents:
                if ingredient in recipe_to_index:
                    adjlist[recipe_to_index[ingredient]].append(index)
                    indegrees[index] += 1
        
        return adjlist, indegrees