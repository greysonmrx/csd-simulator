from numericSystems import NumericSystems

class Application:
    numericSystems = NumericSystems()
    colors = {
        'NORMAL': '\033[0m',
        'GREEN': '\033[1m\033[92m'
    }

    def mainloop(self):
        while True:
            print(self.colors['NORMAL'] + "Escolha uma funcionalidade:\n")
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
                self.relationalAlgebra()

    def measurementUnitsC2onversion(self):
        # Código de conversão entre unidades de medidas
        
        print('measurementUnitsConversion')

    
    def numericSystemsConversion(self):
        while True:
            print(self.colors['NORMAL'] + "\nEscolha uma funcionalidade:\n")
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
        firstBinary = input(self.colors['NORMAL'] + '\nDigite o primeiro binário: ')
        secondBinary = input('Digite o segundo binário: ')

        firstBinary, secondBinary = firstBinary[::-1], secondBinary[::-1]

        deciamlSum = 0

        for index in range(len(firstBinary)):
            digit = int(firstBinary[index])

            if (digit == 0):
                continue

            deciamlSum += (digit * 2) ** index

        for index in range(len(secondBinary)):
            digit = int(secondBinary[index])

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

    def relationalAlgebra(self):
        # Código de expressão da álgebra relacional
        print('relationalAlgebra')

app = Application()

app.mainloop()