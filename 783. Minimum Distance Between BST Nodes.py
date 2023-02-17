'''
https://leetcode.com/problems/minimum-distance-between-bst-nodes
Easy
Approach: DFS
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = float("-inf")

        def dfs(node):
            nonlocal prev
            if not node:
                return float("inf")
            min_diff = dfs(node.left)
            min_diff = min(min_diff, node.val - prev)
            prev = node.val
            min_diff = min(min_diff, dfs(node.right))
            return min_diff

        return dfs(root)