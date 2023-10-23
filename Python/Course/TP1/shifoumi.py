import random

def shifoumi():
    shots = ["pierre", "feuille", "ciseaux"]
    bot = shots[random.randint(0, 2)]
    scoreBot, score = (0, 0)
    while scoreBot < 2 and score < 2:
        inputShot = str(input("Fill with shot (Pierre/Feuille/Ciseaux) : ")).lower()
        while inputShot not in shots:
            inputShot = str(input("Fill with shot (Pierre/Feuille/Ciseaux) : ")).lower()
        print(f'Bot : {bot} - {inputShot} : You')
        if bot == inputShot:
            print("égalité")
        elif (
            (inputShot == shots[0] and bot == shots[2]),
            (inputShot == shots[1] and bot == shots[0]),
            (inputShot == shots[2] and bot == shots[1]),
        ):
            score = score + 1
            if score < 2:
                print("Round win")
        else:
            if scoreBot < 2:
                print("Round lose")
            scoreBot = scoreBot + 1
        print(f'Bot : {scoreBot} - {score} : You')
    if score > scoreBot: 
        print("You win !")
    else:
        print("You lose")

shifoumi()