'''
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
Medium
Approach: Greedy
'''

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        capacity = [capacity[i] - rocks[i] for i in range(len(capacity))]
        capacity.sort()
        full_capacity = 0
        for c in capacity:
            if additionalRocks - c >= 0:
                additionalRocks -= c
                full_capacity += 1
        return full_capacity
                
