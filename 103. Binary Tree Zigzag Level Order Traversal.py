'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
Medium
Approach: BFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([root])
        zigzag = []
        level = 0

        while queue:

            level_size = len(queue)
            level_order = []

            for i in range(level_size):
                node = queue.popleft()
                if not node:
                    continue
                if level % 2 == 0:
                    level_order = level_order + [node.val]
                else:
                    level_order = [node.val] + level_order
                queue.append(node.left)
                queue.append(node.right)
            level += 1
            if len(level_order) > 0:
                zigzag.append(level_order)
                
        return zigzag