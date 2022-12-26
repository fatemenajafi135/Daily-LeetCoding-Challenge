'''
https://leetcode.com/problems/jump-game/
Medium
Approach: Dynamic Programming
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = len(nums) * [0]        
        if len(nums) < 2:
            return True
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if not dp[i - 1]:
                return False
            dp[i] = max(dp[i - 1] - 1, nums[i])
        return True
