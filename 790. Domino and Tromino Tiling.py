'''
https://leetcode.com/problems/domino-and-tromino-tiling/
Medium
Approach: Dynamic Programming
'''

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        mode = 10**9 + 7
        dp1, dp2, dp3 = 1, 2, 5
        for i in range(4, n + 1):
            dp1, dp2, dp3 = dp2, dp3, (dp3 * 2 + dp1) % mode
        return dp3
