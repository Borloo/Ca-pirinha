first_name = "Clément"
last_name = 'Pages'

print(f'{first_name} {last_name}')

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

def multiplicationTable():
    inputNumber = int(input("Which table show ? "))
    datas = []
    for i in range(1, 10):
        data = i * inputNumber
        if (data % 3) == 0:
            data = f'{data}*'
        datas.append(data)
    return datas

# findTheNumber()
# print(keepUniqueValue([1, 5, 7, 1, 5]))
print(multiplicationTable())