customers = {1: {
    "lastname": "Doe",
    "firstname": "John",
    "old": 21,
    "email": "john.doe@xyz.com",
    "hobbies": {"Karaté", "Tennis"} 
    },2: {
    "lastname": "Stewart",
    "firstname": "Jane",
    "old": 26,
    "email": None,
    "hobbies": {"Danse", "Peinture", "Chant"} 
    },3: {
    "lastname": "Tardieu",
    "firstname": "Olivier",
    "old": 32,
    "email": "olivier.tardieux@xyz.com",
    "hobbies": None
    }
}

def translateNumberToChar():
    inputNum = [*str(input("Fill with phone number : "))]
    dico = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    numChar = ""
    for number in inputNum:
        numChar = f'{numChar} {dico[int(number)]}'
    return numChar

def analyseFreqText():
    inputText = [*str(input("Fill with text : ").lower())]
    dico = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    for char in inputText:
        if char not in inputText:
            dico[f'{char}'] = dico[f'{char}'] + 1
    return dico

# print(translateNumberToChar())
print(analyseFreqText())