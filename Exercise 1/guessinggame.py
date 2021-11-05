import random
b = random.randint(1,100)

while True :
    a = int(input('Pick a number (1-100) : '))

    if a == b :
        print("Congratulations, you guessed correctly !")
        break
    elif a > b :
        print("Your number is too high, guess again !")
    elif a < b :
        print("Your number is too low, guess again !")