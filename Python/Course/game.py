##Jeu plus ou moins##
import random
print(f'1 - Facile 0-10'
      f' 2 - Moyen 0-100'
      f' 3 - Difficile 0-1000')

difficulty = int(input("Choisir une difficulté : "))
random_number = 0
user_try = 0

if difficulty == 1:
    random_number = random.randint(0, 10)
elif difficulty == 2:
    random_number = random.randint(0, 100)
elif difficulty == 3:
    random_number = random.randint(0, 1000)


while 1:
    user_number = int(input("Entrer un nombre : "))

    if user_number < random_number:
        print(f'Le nombre est plus grand que {user_number}')
        user_try += 1
    elif user_number > random_number:
        print(f'Le nombre est plus petit que {user_number}')
        user_try += 1
    elif user_number == random_number:
        user_try += 1
        print(f'Bravo, vous avez trouvé en {user_try}')
        break
