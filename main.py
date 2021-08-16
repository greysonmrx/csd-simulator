from logicalPorts import LogicalPorts
from numericSystems import NumericSystems
from booleanAlgebra import BooleanAlgebra
from measurementUnits import MeasurementUnits

class Application:
    numericSystems = NumericSystems()
    booleanAlgebra = BooleanAlgebra()
    logicalPorts = LogicalPorts()
    measurementUnits = MeasurementUnits()

    def mainloop(self):
        while True:
            print("Escolha uma funcionalidade:\n")
            print("  1 - Conversão entre unidades de medida de informação")
            print("  2 - Conversão entre bases numéricas")
            print("  3 - Soma de binários")
            print("  4 - Funções equivalentes as portas lógicas")
            print("  5 - Expressão da álgebra relacional")
            print("  6 - Sair")

            selectedOption = int(input("\nSelecione uma opção: "))

            try:
                if (int(selectedOption) > 6 or int(selectedOption) < 1):
                    return print('\nSelecione uma opção válida!\n')
            except:
                return print('\nSelecione uma opção válida!\n')

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

    def measurementUnitsConversion(self):
        print("\nSelecione a unidade de medida para qual fornecerá um valor:\n")
        print("  1 - Byte")
        print("  2 - Kylobyte")
        print("  3 - Megabyte")
        print("  4 - Gigabyte")
        print("  5 - Terabyte")
        print("  6 - Petabyte")
        print("  7 - Exabyte")
        print("  8 - Zettabyte")
        print("  9 - Yotabyte")

        _from = input("\nSelecione uma opção: ")

        print("\nSelecione a unidade de medida para qual deseja converter:\n")
        print("  1 - Byte")
        print("  2 - Kylobyte")
        print("  3 - Megabyte")
        print("  4 - Gigabyte")
        print("  5 - Terabyte")
        print("  6 - Petabyte")
        print("  7 - Exabyte")
        print("  8 - Zettabyte")
        print("  9 - Yotabyte")

        _to = input("\nSelecione uma opção: ")

        try:
            if (int(_from) > 9 or int(_from) < 1 or int(_to) > 9 or int(_to) < 1):
                return print('\nSelecione uma opção válida!\n')
        except:
            return print('\nSelecione uma opção válida!\n')

        measurementUnitsLabels = {
            '1': 'Byte',
            '2': 'Kylobyte',
            '3': 'Megabyte',
            '4': 'Gigabyte',
            '5': 'Terabyte',
            '6': 'Petabyte',
            '7': 'Exabyte',
            '8': 'Zettabyte',
            '9': 'Yotabyte'
        }

        value = int(input('\nDigite o valor em {}s: '.format(measurementUnitsLabels[_from])))

        _from = measurementUnitsLabels[_from].lower()
        _to = measurementUnitsLabels[_to].lower()

        convertedValue = self.measurementUnits.convert(value, _from, _to)
        
        print("\n{} {}s equivalem a {} {}s\n".format(value, _from.title(), convertedValue, _to.title()))

    def numericSystemsConversion(self):
        while True:
            print("\nEscolha uma funcionalidade:\n")
            print(" 1 - Binário (base 2)")
            print(" 2 - Octal (base 8)")
            print(" 3 - Decimal (base 10)")
            print(" 4 - Hexadecimal (base 16)")
            print(" 5 - Voltar para o menu principal")

            option = int(input("\nEscolha uma opção: "))

            try:
                if (int(option) > 5 or int(option) < 1):
                    return print('\nSelecione uma opção válida!\n')
            except:
                return print('\nSelecione uma opção válida!\n')

            decimal = 0
            
            if (option == 5):
                break

            if option == 1:
                print("\nVocê escolheu a opção 1 - Binário (base 2)")

                number = int(input("\nDigite seu número em binário: "))

                if (not self.numericSystems.verifyBinary(number)):
                    return print('\nDigite um número binário válido!\n')

                decimal = self.numericSystems.binaryToDecimal(number)

            elif option == 2:
                print("\nVocê escolheu a opção 2 - Octal (base 8)")

                number = int(input("\nDigite seu número em octal: "))

                if (not self.numericSystems.verifyOctal(number)):
                    return print('\nDigite um número octal válido!\n')

                decimal = self.numericSystems.octalToDecimal(number)
                
            elif option == 3:
                print("\nVocê escolheu a opção 3 - Decimal (base 10)")

                decimal = int(input("\nDigite seu número em decimal: "))

                if (not self.numericSystems.verifyDecimal(number)):
                    return print('\nDigite um número decimal válido!\n')

            elif option == 4:
                print("\nVocê escolheu a opção 1 - Hexadecimal (base 16)")

                number = input("\nDigite seu número em hexadecimal: ")

                if (not self.numericSystems.verifyHexadecimal(number)):
                    return print('\nDigite um número hexadecimal válido!\n')

                decimal = self.numericSystems.hexadecimalToDecimal(number.upper())

            binary = self.numericSystems.decimalToBinary(decimal)
            octal = self.numericSystems.decimalToOctal(decimal)
            hexadecimal = self.numericSystems.decimalToHexadecimal(decimal)

            print('\nBinário     -> {}'.format(binary))
            print('Octal       -> {}'.format(octal))
            print('Decimal     -> {}'.format(decimal))
            print('Hexadecimal -> {}\n'.format(hexadecimal))

    def sumOfBinaries(self):
        firstBinary = input('\nDigite o primeiro binário: ')

        if (not self.numericSystems.verifyBinary(firstBinary)):
            return print('\nDigite um número binário válido!\n')

        secondBinary = input('Digite o segundo binário: ')

        if (not self.numericSystems.verifyBinary(secondBinary)):
            return print('\nDigite um número binário válido!\n')

        binaries = [firstBinary[::-1], secondBinary[::-1]]

        deciamlSum = 0

        for binary in binaries:
            for index in range(len(binary)):
                digit = int(binary[index])

                if (digit == 0):
                    continue

                deciamlSum += (digit * 2) ** index

        binarySum = self.numericSystems.decimalToBinary(deciamlSum)

        print('\nResultados da soma: ')
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

            try:
                if (int(option) > 7 or int(option) < 1):
                    return print('\nSelecione uma opção válida!\n')
            except:
                return print('\nSelecione uma opção válida!\n')
            
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
        expression = input('\nDigite a expressão: ').upper()

        if (not self.booleanAlgebra.parenthesesIsBalanced(expression)):
            return print('\nExpressão inválida!\n')

        operators = ['AND', 'OR', 'XOR', 'NAND']

        formattedExpression = expression.strip()
        formattedExpression = formattedExpression.replace('(', ' ')
        formattedExpression = formattedExpression.replace(')', ' ')
        formattedExpression = ' '.join(formattedExpression.split())
        splittedExpression = formattedExpression.split(' ')

        if (splittedExpression[0] in operators or splittedExpression[len(splittedExpression) - 1] in operators):
            return print('\nExpressão inválida!\n')

        index = 0

        for value in splittedExpression:
            if (index != 0):
                previousValue = splittedExpression[index - 1]

                if (value in operators):
                    if (previousValue in operators or previousValue == 'NOT'):
                        return print('\nExpressão inválida!\n')
                elif (previousValue in operators and value in operators):
                    return print('\nExpressão inválida!\n')
                elif (value == 'NOT' and (not previousValue in operators and previousValue != 'NOT')):
                    return print('\nExpressão inválida!\n')
                elif (value != 'NOT' and previousValue != 'NOT' and (not previousValue in operators)):
                    return print('\nExpressão inválida!\n')
            
            index += 1

        return print('\nExpressão válida!\n')

app = Application()

app.mainloop()
