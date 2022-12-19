'''
https://leetcode.com/problems/find-if-path-exists-in-graph
Easy
Approach: disjoint set
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        parent = [i for i in range(n)]        
        for u, v in edges:
            if find(u) != find(v):
                parent[find(v)] = parent[find(u)]
        
        return find(source) == find(destination)       
