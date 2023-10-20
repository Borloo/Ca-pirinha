import random

def convertSpeedKmToM():
    inputSpeed = float(input("Enter a speed in km/h : "))
    calculatedSpeed = inputSpeed / 1.609
    return f'{inputSpeed} km/h => {calculatedSpeed: .2f} m/h'

def findTheNumber():
    inputLevel = int(input("Niveau 1/2/3 ? "))
    match inputLevel:
        case 1:
            limit = 10
        case 2:
            limit = 100
        case 3:
            limit = 1000
    numberToFind = random.randint(0, limit)
    isFind = False
    tryToFind = 0
    while isFind == False:
        inputNumber = int(input("Enter a number : "))
        if inputNumber < numberToFind:
            print("+")
        elif inputNumber > numberToFind:
            print("-")
        else:
            isFind = True
        tryToFind = tryToFind + 1
    print(f'Congratulation ! Try : {tryToFind}')

def keepUniqueValue(datas):
    finalDatas = []
    isIn = False
    for data in datas:
        for finalData in finalDatas:
            if data == finalData:
                isIn = True
        if isIn == False:
            finalDatas.append(data)
        isIn = False
    return finalDatas

findTheNumber()
# print(keepUniqueValue([1, 5, 7, 1, 5]))