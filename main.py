class Application:
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

    def measurementUnitsConversion(self):
        # Código de conversão entre unidades de medidas
        
        print('measurementUnitsConversion')

    
    def numericSystemsConversion(self):
        # Código de conversão entre bases numéricas
        print('numericSystemsConversion')        
    
    def sumOfBinaries(self):
        firstBinary = input()
        secondBinary = input()

        firstBinary, secondBinary = firstBinary[::-1], secondBinary[::-1]

        sum = 0

        for index in range(len(firstBinary)):
            digit = int(firstBinary[index])

            if (digit == 0):
                continue

            sum += (digit * 2) ** index

        for index in range(len(secondBinary)):
            digit = int(secondBinary[index])

            if (digit == 0):
                continue

            sum += (digit * 2) ** index

        print('|-------------------------|')
        print('|        CONVERSÃO        |')
        print('|-------------------------|')
        print('| Binário -> {}           |'.format(sum))
        print('| Decimal -> {}           |'.format(sum))
        print('|-------------------------|')
    
    def logicalPorts(self):
        # Código de funções equivalentes as portas lógicas
        print('logicalPorts')

    def relationalAlgebra(self):
        # Código de expressão da álgebra relacional
        print('relationalAlgebra')

app = Application()

app.mainloop()