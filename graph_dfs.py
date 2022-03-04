class Solution851:
    # 851. Loud and Rich
    # https://leetcode.com/problems/loud-and-rich/
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        node_to_richer = self.get_node_to_richer(richer)
        answer = [-1] * len(quiet)
        
        for i in range(len(quiet)):
            self.get_ans(i, answer, node_to_richer, quiet)
        
        return answer
    
    def get_ans(self, i, answer, node_to_richer, quiet):
        if answer[i] != -1:
            return answer[i]
        
        answer[i] = i
        for richer_node in node_to_richer.get(i, []):
            # iterate through the people who are directly richer than self, and update self (answer[i]) by comparing 
            if quiet[self.get_ans(richer_node, answer, node_to_richer, quiet)] < quiet[answer[i]]:
                answer[i] = answer[richer_node]
        
        return answer[i] 
    
    
    def get_node_to_richer(self, richer):
        node_to_richer = {}
        for richer_node, node in richer:
            if node in node_to_richer:
                node_to_richer[node].append(richer_node)
            else:
                node_to_richer[node] = [richer_node]
        return node_to_richer


class Solution797:
    # 797. All Paths From Source to Target
    # https://leetcode.com/problems/all-paths-from-source-to-target/
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        results = []
        self.dfs(0, len(graph) - 1, graph, [0], results, set([0]))
        return results
    
    
    def dfs(self, start, target, graph, curr_path, results, visited):
        if start == target:
            # remember to make deep copy whenever append a list
            results.append(curr_path[:])
            return
        
        for neighbor in graph[start]:
            if neighbor in visited:
                continue
            
            curr_path.append(neighbor)
            visited.add(neighbor)
            self.dfs(neighbor, target, graph, curr_path, results, visited)
            curr_path.pop()
            visited.remove(neighbor)