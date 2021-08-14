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

print()