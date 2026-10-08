import random

number = random.randint(1, 25)

for i in range(5):
    guess = int(input("Guess the number: "))

    if guess < number:
        print("Too low!")

    elif guess > number:
        print("Too high!")

    else:
        print("Correct!")
        break
else:
    print("The correct answer was", number)