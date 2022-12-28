'''
https://leetcode.com/problems/remove-stones-to-minimize-the-total/
Medium
Approach: Greedy
'''

import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        
        for _ in range(k):
            top = -heapq.heappop(heap)
            heapq.heappush(heap, -(top - top // 2))
        
        return -sum(heap)
