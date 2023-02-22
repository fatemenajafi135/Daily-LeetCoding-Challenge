'''
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
Medium
Approach: Greedy and Binary Search
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(max(weights), sum(weights) // days)
        right = sum(weights)

        def helper(target):
            d = 1
            total = 0
            for weight in weights:
                if total + weight <= target:
                    total += weight
                else:
                    d += 1
                    total = weight
            if d <= days:
                return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1

        return left
