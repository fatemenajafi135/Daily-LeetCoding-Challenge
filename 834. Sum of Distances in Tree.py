'''
https://leetcode.com/problems/sum-of-distances-in-tree/  
Hard
Approach: Dynamic Programming
'''

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        @cache
        def dp(a,b):
            total, nodes = 1, 1
            for i in graph[b]:
                if i != a:
                    x, y = dp(b,i)
                    total += x + y
                    nodes += y
            return total, nodes
            
        graph = defaultdict(list)
        ans = []
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for i in range(n):
            ans.append(sum([dp(i,j)[0] for j in graph[i]]))
        return ans
