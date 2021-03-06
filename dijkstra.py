import heapq
class Solution1134:
    # 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
    # https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        city_to_reachables = {}
        adjlist = self.get_adjlist(edges)
        
        for s in range(n):
            city_to_reachables[s] = 0
            self.dijkstra(s, n, adjlist, city_to_reachables, distanceThreshold)
        
        min_num = float("inf")
        min_num_city = None
        for city in city_to_reachables:
            if city_to_reachables[city] <= min_num:
                min_num = city_to_reachables[city]
                min_num_city = city
        
        return min_num_city
            
    
    def dijkstra(self, s, n, adjlist, city_to_reachables, distanceThreshold):
        heap = [(0, s)]
        d = {i: float("inf") for i in range(n)}
        d[s] = 0
        visited = set()
        
        while heap:
            min_dist, curr = heapq.heappop(heap)
            
            if curr in visited:
                continue
                
            visited.add(curr)
            
            for weight, neighbor in adjlist.get(curr, []):
                if neighbor in visited:
                    continue 
                if d[curr] + weight < d[neighbor]:
                    d[neighbor] = d[curr] + weight
                heapq.heappush(heap, (d[neighbor], neighbor))
        
        for key in d:
            if key == s:
                continue
            if d[key] <= distanceThreshold:
                city_to_reachables[s] += 1
        
    
    def get_adjlist(self, edges):
        adjlist = {}
        for u, v, weight in edges:
            self.add_to_adjlist(u, v, weight, adjlist)
            self.add_to_adjlist(v, u, weight, adjlist)
        return adjlist
            
    
    def add_to_adjlist(self, u, v, weight, adjlist):
        if u in adjlist:
            adjlist[u].append((weight, v))
        else:
            adjlist[u] = [(weight, v)]
        
        
class Solution1786:
    # 1786. Number of Restricted Paths From First to Last Node
    # https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        adjlist = collections.defaultdict(list)
        for u, v, weight in edges:
            adjlist[u].append((v, weight))
            adjlist[v].append((u, weight))
        
        d = {i: float("inf") for i in range(1, n + 1)}
        d[n] = 0
        
        ways = {i: 0 for i in range(1, n + 1)}
        ways[n] = 1
        
        heap = [(0, n)]
        visited = set()
        
        while heap:
            weight, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            
            for neighbor, weight in adjlist[u]:
                if neighbor in visited:
                    continue
                    
                if d[u] + weight < d[neighbor]:
                    d[neighbor] = d[u] + weight
                
                if d[neighbor] > d[u]:
                    ways[neighbor] = (ways[neighbor] + ways[u]) % (10**9 + 7)

                heapq.heappush(heap, (d[neighbor], neighbor))
        
        return ways[1]
              
        