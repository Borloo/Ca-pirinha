import random

def convertSpeedKmToM():
    inputSpeed = float(input("Enter a speed in km/h : "))
    calculatedSpeed = inputSpeed / 1.609
    return f'{inputSpeed} km/h => {calculatedSpeed: .2f} m/h'

def findTheNumber():
    inputLevel = int(input("Niveau 1/2/3 ? "))
    limit = 0
    match inputLevel:
        case 1:
            limit = 10
        case 2:
            limit = 100
        case 3:
            limit = 1000
    numberToFind = random.randint(0, limit)
    isFind = False
    while isFind == False:
        inputNumber = int(input("Enter a number : "))
        if inputNumber < numberToFind:
            print("+")
        elif inputNumber > numberToFind:
            print("-")
        else:
            isFind = True
    print("gg")

findTheNumber()