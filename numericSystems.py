class NumericSystems:
    def decimalToBinary(self, number):
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
    
    def binaryToDecimal(self, number):
        j, result = 0, 0

        for i in reversed(str(number)):
            i = int(i)
            result += (i*(2**j))
            j += 1

        return result
    
    def decimalToHexadecimal(self, number):
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
    
    def hexadecimalToDecimal(self, number):
        result = 0
        j = 0
        hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15 }

        for i in reversed(str(number)):
            result += hex[i] *(16**j)
            j += 1

        return result

    def decimalToOctal(self, number):
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
    
    def octalToDecimal(self, number):
        j, result = 0, 0

        for i in reversed(str(number)):
            i = int(i)
            result += (i*(8**j))
            j += 1

        return result
    
    def verifyBinary(self, number):
        for digit in str(number):
            try:
                if 0 > int(digit) or 1 < int(digit):
                    return False
            except:
                return False
        
        return True

    def verifyOctal(self, number):
        for digit in str(number):
            try:
                if 0 > int(digit) or 7 < int(digit):
                    return False
            except:
                return False
        
        return True
    
    def verifyDecimal(self, number):
        for digit in str(number):
            try:
                if 0 > int(digit) or 9 < int(digit):
                    return False
            except:
                return False
    
    def verifyHexadecimal(self, number):
        validChars = ['A', 'B', 'C', 'D', 'E', 'F']

        for digit in str(number):
            try:
                if 0 > int(digit) or 9 < int(digit):
                    return False
            except:
                if (not digit.upper() in validChars):
                    return False
        
        return True
