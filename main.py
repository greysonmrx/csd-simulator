from numericSystems import NumericSystems
from booleanAlgebra import BooleanAlgebra

class Application:
    numericSystems = NumericSystems()
    booleanAlgebra = BooleanAlgebra()
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
                self.logicalPorts()
            elif (selectedOption == 5):
                self.booleanAlgebraExpression()

    def measurementUnitsC2onversion(self):
        # Código de conversão entre unidades de medidas
        
        print('measurementUnitsConversion')

    
    def numericSystemsConversion(self):
        while True:
            print(self.colors['DEFAULT'] + "\nEscolha uma funcionalidade:\n")
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
    
    def logicalPorts(self):
        # Código de funções equivalentes as portas lógicas
        print('logicalPorts')

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