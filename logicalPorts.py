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
    
    #porta nor
    def norOutput(self, logical_inputs):
        return not_convert(or_convert(logical_inputs))

    #porta nand
    def nandOutput(self, logical_inputs):
        return not_convert(and_convert(logical_inputs))

    
    def xorOutput(self, logical_inputs):
        if len(logical_inputs) == 1:
            return int(logical_inputs)
        
        a = int(logical_inputs[0])
        for i in range(len(logical_inputs)):
            for j in range(len(logical_inputs)):
                a = int(logical_inputs[i])
                b = int(logical_inputs[j])

                if a != b:  return 1
                else:   output = 0
        
        return output