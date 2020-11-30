from art import logo
import random 


guess_count = []


def difficulty(level):
  if level == 'hard':
    guess_count.append(5)
  elif level == 'easy':
    guess_count.append(10)
  
def play():
  guess_answer = False
  # iterate until guess_answer is correct
  while guess_answer == False : 
    print(logo)
    print("Welcome to guess my number game!")
    print("I am thinking of number from 1 to 100.")
    guess_number = random.randint(0,10)
    level = input("Choose your difficulty type hard or easy: ")
    difficulty(level)
    print(f"You have {(guess_count[0])} attemps to guess the number")
    # number of iteration is equal to level of guess_count
    for i in range(guess_count[0]) :
      make_guess = int(input("Make a guess: "))
      if make_guess == guess_number :
        print("You got it!")
        guess_answer = True
        break
      elif make_guess != guess_number :
        if make_guess < guess_number :
          print("Too low")
        elif make_guess > guess_number :
          print("Too high")
        print("You guess it wrong!")  
  
while input("Let's play a game? 'y' or 'n' : ") == 'y' :
  play()
  