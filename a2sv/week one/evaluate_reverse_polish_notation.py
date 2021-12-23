class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpn_stack = []
        operand1, operand2 = 0, 0
        
        for x in tokens:
            if x == '+':
                operand2 = rpn_stack.pop()
                operand1 = rpn_stack.pop()
                rpn_stack.append(operand1 + operand2) 
            elif x == '-':
                operand2 = rpn_stack.pop()
                operand1 = rpn_stack.pop()
                rpn_stack.append(operand1 - operand2) 
            elif x == '*':
                operand2 = rpn_stack.pop()
                operand1 = rpn_stack.pop()
                rpn_stack.append(operand1 * operand2) 
            elif x == '/':
                operand2 = rpn_stack.pop()
                operand1 = rpn_stack.pop()
                rpn_stack.append(int(operand1 / operand2)) 
            else:
                rpn_stack.append(int(x))
        return int(rpn_stack[0])
        