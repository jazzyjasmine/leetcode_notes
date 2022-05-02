import collections
from typing import List


class Solution261BFS:
    # 261. Graph Valid Tree
    # https://leetcode.com/problems/graph-valid-tree/
    """BFS"""
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        queue = collections.deque([(-1, 0)])
        visited = set([0])
        adjlist = collections.defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        while queue:
            parent, curr = queue.popleft()
            for neighbor in adjlist[curr]:
                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False
                
                queue.append((curr, neighbor))
                visited.add(neighbor)
        
        return len(visited) == n


class Solution261DFS1:
    """
    DFS 

    add node to visited after calling dfs function
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = collections.defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visited = set()
        return self.dfs(0, -1, visited, adjlist) and len(visited) == n
    
    
    def dfs(self, node, parent, visited, adjlist):
        visited.add(node)
        
        for neighbor in adjlist[node]:
            # exclude the case when neighbor == parent
            # for undirected graph, each edge has two directions
            if neighbor == parent:
                continue
            
            if neighbor in visited:
                return False
            
            # for all neighbors, if one neighbor returns False, the current dfs returns False
            if not self.dfs(neighbor, node, visited, adjlist):
                return False
        
        return True


class Solution261DFS2:
    """
    DFS

    add node to visited before calling dfs function
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = collections.defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        visited = set([0])
        return self.dfs(0, -1, visited, adjlist) and len(visited) == n
    
    
    def dfs(self, node, parent, visited, adjlist):
        for neighbor in adjlist[node]:
            if neighbor == parent:
                continue
            
            if neighbor in visited:
                return False
            
            visited.add(neighbor)
            if not self.dfs(neighbor, node, visited, adjlist):
                return False
        
        return True


class Solution261DFSColor:
    """
    DFS with color

    white: not yet visited
    gray: visited, probing its descendents
    black: visited, and finished probing
    """
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = collections.defaultdict(list)
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        color = {i: "white" for i in range(n)}
        
        self.dfs(0, -1, color, adjlist)
        
        return all(color[i] == "black" for i in color)

    
    def dfs(self, node, parent, color, adjlist):
        color[node] = "gray"
        
        for neighbor in adjlist[node]:
            if neighbor == parent:
                continue
            
            if color[neighbor] == "black":
                # if neighbor is black, that neighbor is in a different connected component
                continue
            
            if color[neighbor] == "gray":
                # if neighbor is gray, that neighbor is in same connected component and thus forms a cycle
                return
            
            self.dfs(neighbor, node, color, adjlist)
        
        color[node] = "black"