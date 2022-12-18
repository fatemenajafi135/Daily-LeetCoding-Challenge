'''
https://leetcode.com/problems/daily-temperatures
Medium
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = len(temperatures) * [0]
        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                top_index = stack.pop()
                answer[top_index] = i - top_index
            stack.append(i)
        return answer
