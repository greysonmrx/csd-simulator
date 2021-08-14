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

    def measurementUnitsC2onversion(self):
        # Código de conversão entre unidades de medidas
        
        print('measurementUnitsConversion')

    
    def numericSystemsConversion(self):
        #convert decimal to binary
        def decimal2binary(number):
            remainder_list = []
            result = ''

            if number == 0 or number == 1:
                return number
            
            while number > 0:
                remainder = number % 2
                remainder_list.append(remainder)
                number = number // 2
            
            for i in reversed(remainder_list):
                result += str(i)
            return int(result)

        #convert binary to decimal
        def binary2decimal(number):
            j, result = 0, 0
            for i in reversed(str(number)):
                i = int(i)
                result += (i*(2**j))
                j += 1
            return result

        #convert decimal to hexadecimal
        def decimal2hex(number):
            remainder_list = []
            result = ''

            hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', '6': 6, 7: '7', 8: '8', 9: '9',
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }

            if number == 0 or number == 1:
                return number
            
            while number > 0:
                remainder = number % 16
                remainder_list.append(hex[remainder])
                number = number // 16
            
            for i in reversed(remainder_list):
                result += str(i)

            return result

        #convert hexadecimal to decimal
        def hex2decimal(number):
            result = 0
            j = 0
            hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

            for i in reversed(str(number)):
                result += hex[i] *(16**j)
                j += 1
            return result

        #convert decimal to octal
        def decimal2octal(number):
            remainder_list = []
            result = ''

            if number == 0 or number == 1:
                return number
            
            while number > 0:
                remainder = number % 8
                remainder_list.append(remainder)
                number = number // 8
            
            for i in reversed(remainder_list):
                result += str(i)
            return int(result)

        #convert octal to decimal
        def octal2decimal(number):
            j, result = 0, 0
            for i in reversed(str(number)):
                i = int(i)
                result += (i*(8**j))
                j += 1
            return result
        while True:
            print("Escolha uma funcionalidade:\n")
            print(" 1 - Binário (base 2)")
            print(" 2 - Octal (base 8)")
            print(" 3 - Decimal (base 10)")
            print(" 4 - Hexadecimal (base 16)")
            print(" 5 - Voltar para o menu principal")
            option = int(input("Escolha uma opção: "))
            
            if (option == 5):
                break

            if option == 1:
                print("\nVocê escolheu a opção 1 - Binário (base 2)")
                number = int(input("Digite seu número em binário: "))
                decimal = binary2decimal(number)

            elif option == 2:
                print("\nVocê escolheu a opção 2 - Octal (base 8)")
                number = int(input("Digite seu número em octal: "))
                decimal = octal2decimal(number)
                
            elif option == 3:
                print("\nVocê escolheu a opção 3 - Decimal (base 10)")
                decimal = int(input("Digite seu número em decimal: "))

            elif option == 4:
                print("\nVocê escolheu a opção 1 - Hexadecimal (base 16)")
                number = input("Digite seu número em hexadecimal: ")
                decimal = hex2decimal(number)

            print("Binario: ", decimal2binary(decimal))
            print("Octal: " , decimal2octal(decimal))
            print("Decimal: ", decimal)
            print("Hexadecimal: ", decimal2hex(decimal))

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