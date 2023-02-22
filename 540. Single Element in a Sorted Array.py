'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
Medium
Approach: Greedy and Binary Search
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=0
        n=len(nums)
        e=len(nums)-1
        while(s<=e):
            mid=s+(e-s)//2
            if((mid-1)>=0 and nums[mid]==nums[mid-1] ):
                period=n-1-(mid)
                if(period%2==1):
                    s=mid+1
                else:
                    e=mid-2                
            elif((mid+1)<n and nums[mid]==nums[mid+1]):
                period=n-1-(mid+1)
                if(period%2==1):
                    s=mid+2
                else:
                    e=mid-1
            else:
                return nums[mid]
        return nums[mid]
