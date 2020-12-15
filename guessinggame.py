import random

def guess(x):
    n = random.randint(1,x)
    guess = 0
    i = 1
    while guess != n:
        guess = int(input('Guess a number between 1 and {}: '.format(x)))
        if guess < n - (x//2):
            print("Your Guess is too low!")
            i += 1
            continue
        if guess > n + (x//2):
            print("Your Guess is too high!")
            i += 1
            continue
        if guess < n:
            print("Your Guess is low.")
            i += 1
        if guess > n:
            print("Your Guess is high.")
            i += 1
        
    print("You guessed it correctly in {} guesses!".format(i))

def computer_guess(x):
    low = 1
    high = x
    n = 1
    feedback = ""
    while feedback != "c":
        guess = random.randint(low,high)
        print("Computer's guess:",guess)
        feedback = input("Enter feedback (H for high, L for low, C for correct: ").lower()
        if feedback == 'h':
            high = guess - 1
            n += 1
        if feedback == "l":
            low = guess + 1
            n += 1
    
    print("Computer guessed it correctly in {} guesses!".format(n))


print("**********Welcome to the Guessing Game**********")
print("**********Guess a Number between 1-100**********")
print("Who's gonna Guess?")
start = input("Press 1 for You or 2 for Computer: ")
if start == "1":
    guess(100)
elif start == "2":
    print("Have a number in your mind & Let the computer guess it..")
    computer_guess(100)
else:
    print("Invalid Input!!")
