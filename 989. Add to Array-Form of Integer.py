'''
https://leetcode.com/problems/add-to-array-form-of-integer/
Easy
Approach: Math
'''

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num)-1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        while k:
            k, d = divmod(k, 10)
            num = [d] + num
        return num
