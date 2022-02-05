import random

#variable to generate random number
x = random.randint(0,100)

string = "WELCOME TO THE NUMBER GUESSING GAME!"
print(string.center(24))
print('***********************************************')
name = input("What is your name?")
intro = "Can you guess the same number that the computer is thinking of?"
print("Hi, "+ name+"!", intro)
print()

#empty list to store guesses
incorrect_answers=[]
while True:
    guess = int(input("Guess a number between 0 and 100:")) #accepts the user's input as an integer
    incorrect_answers.append(guess) #adds incorrect guesses to the list
    if guess < 0 or guess > 100:
        print("Keep your guesses between 0 and 100.")
        print()
        continue
    if guess < x:
        print("Hmmm...higher! Your guess is too low.")
        print()
    if guess > x:
        print("Hmmm...lower! Your guess is too high.")
        print()
    if guess == x:
        print("Bravo! You guessed the correct answer in", len(incorrect_answers), "guesses.")
        print("Your guesses were:", incorrect_answers)
        break
