class LogicalPorts:
    #not ports
    def notOutput(self, logical_input):
    
        if len(str(logical_input)) != 1:
            return "Entrada Inválida"

        logical_input = int(logical_input)
            
        if logical_input == 0:  logical_input = 1
        elif logical_input == 1:  logical_input = 0

        return logical_input

    #or ports
    def orOutput(self, logical_inputs):
        a = int(logical_inputs[0])
        for i in range(1, len(logical_inputs)):
            b = int(logical_inputs[i])
            a = a or b

        return a

    #and ports
    def andOutput(self, logical_inputs):
        a = int(logical_inputs[0])
        for i in range(1, len(logical_inputs)):
            b = int(logical_inputs[i])
            a = a and b

        return a
    
    #nor ports
    def norOutput(self, logical_inputs):
        a = int(logical_inputs[0])
        for i in range(1, len(logical_inputs)):
            b = int(logical_inputs[i])
            a = a or b
            a = self.notOutput(a)

        return a

    #nand ports
    def nandOutput(self, logical_inputs):
        a = int(logical_inputs[0])
        for i in range(1, len(logical_inputs)):
            b = int(logical_inputs[i])
            a = a and b
            a = self.notOutput(a)

        return a

    #xor ports
    def xorOutput(self, logical_inputs):
        a = int(logical_inputs[0])
        for i in range(1, len(logical_inputs)):
            b = int(logical_inputs[i])
            if (a == b):    a = 0
            else:   a = 1            
        return a