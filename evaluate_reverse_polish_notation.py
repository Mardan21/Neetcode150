import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        rpn_stack = []
 
        for i in range(len(tokens)):
            if tokens[i] in operations:
                val_one = int(rpn_stack.pop())
                val_two = int(rpn_stack.pop())
                res = operations[tokens[i]](val_two, val_one)
                rpn_stack.append(res)
            else:
                rpn_stack.append(tokens[i])
        
        return int(rpn_stack.pop())
