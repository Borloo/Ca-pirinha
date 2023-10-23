import random
import string
import itertools
import time

characters = string.ascii_letters + string.digits + '()[]:;!'
long = 5

def generate_password():
    password = ''.join(random.choice(characters) for _ in range(long))
    return password

def bruteforce_password():
    password_to_find = generate_password()
    chrono = time.time()
    print(f'password to find : {password_to_find}')
    for length in range(1, (long + 1)):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            if password_to_find == password:
                print(f'password to find is : {password}')
                print(f'Time to find : {round(time.time() - chrono, 2)}s')
                break

def calculate_password_combinations():
    characters = 26 + 26 + 10 + 7
    combinations = characters ** long
    return combinations

print(generate_password())
bruteforce_password()
print(f'Combinaison possible : {calculate_password_combinations()}')