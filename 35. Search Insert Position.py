'''
https://leetcode.com/problems/search-insert-position
Easy
Approach: Binary Search
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def search_insert(nums, target, low, high):
            if low > high:
                return low
            place = int((high + low) / 2)
            if nums[place] == target:
                return place
            if nums[place] > target:
                return search_insert(nums, target, low, place-1)
            return search_insert(nums, target, place+1, high)
            
        return search_insert(nums, target, 0, len(nums)-1)