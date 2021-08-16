from logicalPorts import LogicalPorts
from numericSystems import NumericSystems
from booleanAlgebra import BooleanAlgebra

class Application:
    numericSystems = NumericSystems()
    booleanAlgebra = BooleanAlgebra()
    logicalPorts = LogicalPorts()

    colors = {
        'DEFAULT': '\033[0m',
        'GREEN': '\033[1m\033[92m',
        'RED': '\033[1m\033[91m'
    }

    def mainloop(self):
        while True:
            print(self.colors['DEFAULT'] + "Escolha uma funcionalidade:\n")
            print("  1 - Conversão entre unidades de medida de informação")
            print("  2 - Conversão entre bases numéricas")
            print("  3 - Soma de binários")
            print("  4 - Funções equivalentes as portas lógicas")
            print("  5 - Expressão da álgebra relacional")
            print("  6 - Sair")

            selectedOption = int(input("\nSelecione uma opção: "))

            if (selectedOption == 6):
                break

            if (selectedOption == 1):
                self.measurementUnitsConversion()
            elif (selectedOption == 2):
                self.numericSystemsConversion()
            elif (selectedOption == 3):
                self.sumOfBinaries()
            elif (selectedOption == 4):
                self.logicalPortsOutput()
            elif (selectedOption == 5):
                self.booleanAlgebraExpression()

    def measurementUnitsC2onversion(self):
        
        while True:
            print("Escola o tipo de conversão:\n")
            print("  1 - Byte para kyloByte")
            print("  2 - Byte para MegaByte")
            print("  3 - Byte para GigaByte")
            print("  4 - Byte para TeraByte")
            print("  5 - KyloByte para MegaByte")
            print("  6 - MegaByte para KyloByte")
            print("  7 - GigaByte para MegaByte")
            print("  8 - MegaByte para GigaByte")
            print("  9 - GigaByte para TeraByte")
            print("  10 - TeraByte para GigaByte")
            print("  11 - Sair")

            selectedOption = int(input("\nSelecione uma opção: "))
            if (selectedOption == 11):
                break

            if (selectedOption == 1):
                num = int(input("Digite o valor a ser convertido:\n"))
                kb = num/1000
                print("O valor em KiloByte é {}\n".format(kb))
            elif (selectedOption == 2):
                num = int(input("Digite o valor a ser convertido:\n"))
                kb = num/1000
                mb = kb/1000
                print("O valor em MegaBite é {}\n".format(mb))
            elif (selectedOption == 3):
                num = int(input("Digite o valor a ser convertido:\n"))
                kb = num/1000
                mb = kb/1000
                gb = mb/1000
                print("O valor em GigaBite é {}\n".format(gb))
            elif (selectedOption == 4):
                num = int(input("Digite o valor a ser convertido:\n"))
                kb = num/1000
                mb = kb/1000
                gb = mb/1000
                tb = gb/1000
                print("O valor em TeraBite é {}\n".format(tb))
            elif (selectedOption == 5):
                num = int(input("Digite o valor a ser convertido:\n"))
                mb = num/1000
                print("O valor em MegaBite é {}\n".format(mb))
            elif (selectedOption == 6):
                num = int(input("Digite o valor a ser convertido:\n"))
                kb = num*1000
                print("O valor em KiloBite é {}\n".format(kb))
            elif (selectedOption == 7):
                num = int(input("Digite o valor a ser convertido:\n"))
                mb = num/1000
                print("O valor em MegaBite é {}\n".format(mb))
            elif (selectedOption == 8):
                num = int(input("Digite o valor a ser convertido:\n"))
                gb = num*1000
                print("O valor em GigaBite é {}\n".format(gb)) 
            elif (selectedOption == 9):
                num = int(input("Digite o valor a ser convertido:\n"))
                tb = num/1000
                print("O valor em TeraBite é {}\n".format(tb))
            elif (selectedOption == 10):
                num = int(input("Digite o valor a ser convertido:\n"))
                gb = num*1000
                print("O valor em GigaBite é {}\n".format(gb))

    def numericSystemsConversion(self):
        while True:
            print(self.colors['DEFAULT'] + "\nEscolha a base númerica original:\n")
            print(" 1 - Binário (base 2)")
            print(" 2 - Octal (base 8)")
            print(" 3 - Decimal (base 10)")
            print(" 4 - Hexadecimal (base 16)")
            print(" 5 - Voltar para o menu principal")

            option = int(input("\nEscolha uma opção: "))
            decimal = 0
            
            if (option == 5):
                break

            if option == 1:
                print("\nVocê escolheu a opção 1 - Binário (base 2)")

                number = int(input("\nDigite seu número em binário: "))
                decimal = self.numericSystems.binaryToDecimal(number)

            elif option == 2:
                print("\nVocê escolheu a opção 2 - Octal (base 8)")

                number = int(input("\nDigite seu número em octal: "))
                decimal = self.numericSystems.octalToDecimal(number)
                
            elif option == 3:
                print("\nVocê escolheu a opção 3 - Decimal (base 10)")

                decimal = int(input("\nDigite seu número em decimal: "))

            elif option == 4:
                print("\nVocê escolheu a opção 1 - Hexadecimal (base 16)")

                number = input("\nDigite seu número em hexadecimal: ")
                decimal = self.numericSystems.hexadecimalToDecimal(number.upper())

            binary = self.numericSystems.decimalToBinary(decimal)
            octal = self.numericSystems.decimalToOctal(decimal)
            hexadecimal = self.numericSystems.decimalToHexadecimal(decimal)

            print(self.colors['GREEN'] + '\nBinário     -> {}'.format(binary))
            print('Octal       -> {}'.format(octal))
            print('Decimal     -> {}'.format(decimal))
            print('Hexadecimal -> {}\n'.format(hexadecimal))

    def sumOfBinaries(self):
        firstBinary = input(self.colors['DEFAULT'] + '\nDigite o primeiro binário: ')
        secondBinary = input('Digite o segundo binário: ')

        binaries = [firstBinary[::-1], secondBinary[::-1]]

        deciamlSum = 0

        for binary in binaries:
            for index in range(len(binary)):
                digit = int(binary[index])

                if (digit == 0):
                    continue

                deciamlSum += (digit * 2) ** index

        binarySum = self.numericSystems.decimalToBinary(deciamlSum)

        print(self.colors['GREEN'] + '\nResultados da soma: ')
        print('  - Em binário -> {}'.format(binarySum))
        print('  - Em decimal -> {}\n'.format(deciamlSum))
    
    def logicalPortsOutput(self):

        while True:
            print("\nEscolha uma porta:\n")
            print(" 1 - not")
            print(" 2 - or")
            print(" 3 - and")
            print(" 4 - nor")
            print(" 5 - nand")
            print(" 6 - xor")
            print(" 7 - Voltar para o menu principal")

            option = int(input("\nEscolha uma opção: "))
            
            if (option == 7):
                break

            inputs = input("\nEntrada: ")

            if (option == 1):
                logical_output = self.logicalPorts.notOutput(inputs)

            if (option == 2):
                logical_output = self.logicalPorts.orOutput(inputs)

            if (option == 3):
                logical_output = self.logicalPorts.andOutput(inputs)

            if (option == 4):
                logical_output = self.logicalPorts.norOutput(inputs)

            if (option == 5):
                logical_output = self.logicalPorts.nandOutput(inputs)

            if (option == 6):
                logical_output = self.logicalPorts.xorOutput(inputs)
            
            print("Saída -> {}" .format(logical_output))

    def booleanAlgebraExpression(self):
        expression = input(self.colors['DEFAULT'] + '\nDigite a expressão: ').upper()

        if (not self.booleanAlgebra.parenthesesIsBalanced(expression)):
            return print(self.colors['RED'] + '\nExpressão inválida!\n')

        operators = ['AND', 'OR', 'XOR', 'NAND']

        formattedExpression = expression.strip()
        formattedExpression = formattedExpression.replace('(', ' ')
        formattedExpression = formattedExpression.replace(')', ' ')
        formattedExpression = ' '.join(formattedExpression.split())
        splittedExpression = formattedExpression.split(' ')

        if (splittedExpression[0] in operators or splittedExpression[len(splittedExpression) - 1] in operators):
            return print(self.colors['RED'] + '\nExpressão inválida!\n')

        index = 0

        for value in splittedExpression:
            if (index != 0):
                previousValue = splittedExpression[index - 1]

                if (value in operators):
                    if (previousValue in operators or previousValue == 'NOT'):
                        return print(self.colors['RED'] + '\nExpressão inválida!\n')
                elif (previousValue in operators and value in operators):
                    return print(self.colors['RED'] + '\nExpressão inválida!\n')
                elif (value == 'NOT' and (not previousValue in operators)):
                    return print(self.colors['RED'] + '\nExpressão inválida!\n')
                elif (value != 'NOT' and previousValue != 'NOT' and (not previousValue in operators)):
                    return print(self.colors['RED'] + '\nExpressão inválida!\n')
            
            index += 1

        return print(self.colors['GREEN'] + '\nExpressão válida!\n')

app = Application()

app.mainloop()
