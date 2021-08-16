from stack import Stack

class BooleanAlgebra:
    stack = Stack()

    def parenthesesIsBalanced(self, expression):
        self.stack.clear()

        for char in expression:
            if char == '(':
                self.stack.push(char)
            elif char == ')':
                if (self.stack.isEmpty()):
                    return False
                
                self.stack.pop()

        if (self.stack.isEmpty()):
            return True
        
        return False
