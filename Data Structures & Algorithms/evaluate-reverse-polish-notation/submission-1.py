from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # Order matters for subtraction: second popped minus first popped
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                # Order matters for division: second popped divided by first popped
                b, a = stack.pop(), stack.pop()
                # int() in Python truncates toward zero (e.g., -3 // 2 is -2, but int(-3 / 2) is -1)
                stack.append(int(a / b))
            else:
                stack.append(int(token))
        return stack[0]