'''
https://leetcode.com/problems/possible-bipartition
Medium
Approach: DFS
'''

class Solution:
    def dfs(self, i, group):
        if i in self.group_mapping and group != self.group_mapping[i]:
            return False
        self.group_mapping[i] = group
        if i not in self.visited:
            self.visited.add(i)
            for dis in self.graph[i]:
                if not self.dfs(dis, not group): 
                    return False
        return True    
        
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        self.visited, self.group_mapping = set(), {}
        for (u, v) in dislikes:  
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        for i in range(1, N+1):           
            if i not in self.visited:    
                if not self.dfs(i, True):      
                    return False
        return True
