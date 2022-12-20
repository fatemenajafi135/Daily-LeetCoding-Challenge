'''
https://leetcode.com/problems/keys-and-rooms
Medium
Approach: DFS
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = rooms[0]
        visited = set()
        while stack:
            print(stack)
            key = stack.pop()
            if key not in visited and key:
                visited.add(key)
                stack += rooms[key]
        return len(visited) == len(rooms) - 1
