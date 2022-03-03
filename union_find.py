class Solution684:
    # 684. Redundant Connection
    # https://leetcode.com/problems/redundant-connection/
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        parents, ranks = self.makeset(n)
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            uroot = self.find(parents, u)
            vroot = self.find(parents, v)
            if uroot == vroot:
                return edge
            self.union(parents, ranks, uroot, vroot)
        
        return -1
    
    def makeset(self, n):
        return {i: i for i in range(1, n + 1)}, {i: 0 for i in range(1, n + 1)}
    
    def find(self, parents, u):
        while parents[u] != u:
            u = parents[u]
        return u
    
    def union(self, parents, ranks, uroot, vroot):
        if ranks[uroot] < ranks[vroot]:
            parents[uroot] = vroot
        else:
            parents[vroot] = uroot
            if ranks[uroot] == ranks[vroot]:
                ranks[uroot] += 1
        