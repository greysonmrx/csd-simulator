class Stack:
    array = []

    def clear(self):
        self.array = []

    def isEmpty(self):
        return not(len(self.array))
    
    def getTop(self):
        if (len(self.array) > 0):
            return self.array.index(0)
        
        return False
    
    def push(self, element):
        self.array.append(element)

    def pop(self):
        if (not self.isEmpty()):
            return self.array.pop()

        return False