#  Variables.
import random
guess = random.randint(1, 100)  # The random number.
guessed = 0  # Number of guessed time.

#  Basic greetings.
print("Welcome to Guess the Number!\n")
print("let's start!\n")

#  Introduction.
name = str(input("What is your name?: "))
print("Dear ", name, ", please fire your brain cells.")
x = int(input("Guess a number between 1 and 100. Attention, you will have 9 tries!: "))

#  Function in action.
while guessed < 9:
    print()
    guessed = guessed + 1
    if x < guess:
        print()
        x = int(input("Enter a higher number: "))
    elif x > guess:
        print()
        x = int(input("Enter a lower number: "))
    elif x == guess:
        break

if x == guess:
    guessed = str(guessed)
    print("You guessed it! Bravo ", name, "! And you guessed with ", guessed, " turns!")

if x != guess:
    guess = str(guess)
    guessed = str(guessed)
    print("Tough luck ", name, ". The answer is ", guess, ". You wasted ", guessed, "turns")

print("Thank you for your participation!")
