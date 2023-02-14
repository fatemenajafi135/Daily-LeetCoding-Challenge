'''
https://leetcode.com/problems/add-binary
Easy
Approach: math but using python's bin()
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]