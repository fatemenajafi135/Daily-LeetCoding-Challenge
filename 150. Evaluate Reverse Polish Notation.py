class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda right, left: left + right,
            '*': lambda right, left: left * right,
            '-': lambda right, left: left - right,
            '/': lambda right, left: left / right
        }
        stack = []
        for token in tokens:
            if token in operations:
                stack.append(int(operations[token](stack.pop(), stack.pop())))
            else:
                stack.append(int(token))
        return stack[0]
