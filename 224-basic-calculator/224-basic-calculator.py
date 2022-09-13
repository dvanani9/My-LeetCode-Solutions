class Solution:
    def calculate(self, s: str) -> int:
        
        stack = [] 
        number, sign, res = 0, 1, 0

        for char in s: 
            if char.isdigit(): #
                number = number * 10 + int(char)
            elif char == '+' or char == '-':
                res += sign * number
                sign = 1 if char == '+' else -1
                number = 0
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif char == ')':
                res += sign * number
                number = 0
                res *= stack.pop()
                res += stack.pop() 
            else:
                continue

        return res + (number * sign) 