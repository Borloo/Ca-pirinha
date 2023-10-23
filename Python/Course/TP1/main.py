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

def keepUniqueValue(datas: [int]):
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

def moyenneNotes():
    notes = []
    while True:
        try:
            inputNote = int(input("Saisissez une note positive : "))
            if inputNote < 0 or inputNote > 20:
                break  # Sortir de la boucle si la note n'est pas entre 0 et 20
            notes.append(inputNote)
        except ValueError:
            print("Saisissez un entier valide.")

    if len(notes) == 0:
        print("Il n'y a pas de notes ...")
    else:
        moyenne = sum(notes) / len(notes)
        print(f'La moyenne des {len(notes)} notes : {moyenne}') 

def caesarCipher(text: str, offset: int = 1) -> str :
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            index = (ord(char) - ord('a') + offset) % 26
            result += chr(index + ord('a'))
            continue
        elif 'A' <= char <= 'Z':
            index = (ord(char) - ord('a') + offset) % 26
            result += chr(index + ord('A'))
        else:
            result += char
    return result

def ceaserDecipher(text: str) -> list[list[int, str]]:
    result = []
    for i in range(1, 27):
        result.append((i, caesarCipher(text, i)))
    return result

def readFile(path: str):
    try:
        with open(path) as f:
            print(type(f))
            poem = f.read
    except FileNotFoundError:
        poem = None
    return poem

# findTheNumber()
# print(keepUniqueValue([1, 5, 7, 1, 5]))
# print(multiplicationTable())
# moyenneNotes()
# text = "gros caca dans mon cul !?"
# print(caesarCipher(text, 26))
# tab = ceaserDecipher(text)
# for value in tab:
#     print(value)
readFile('./data/poem.txt')