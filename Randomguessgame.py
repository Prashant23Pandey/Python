import random
print("Welcome to the guessing game")
number = random.randint(1,30)
while True:
    guess = int(input("Guess a number between 1 to 30: \n")) 
    if guess == number:
        print("You Won!!")
        break
    elif guess<number:
        print("Too low try again")
    else:
        print("Try Again")