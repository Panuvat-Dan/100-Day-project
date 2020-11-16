import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_selection = [rock,paper,scissors]
### people_choose
your_selection = input("Please select what in your mind? type 0 for'rock',type 1 for 'paper',type 2 for 'scissors': ")
output_your_selection = list_selection[int(your_selection)].lower()
people = (f"Your choose : {output_your_selection}")
print(people)

### computer_choose
computer_choose = random.randint(0,2)
computer_convert = list_selection[computer_choose]
bot = (f"Computer choose : {computer_convert} ")
print(bot)

## create_condition as rock,paper,scissors international game rule

if int(your_selection) >= 3 or int(your_selection) < 0: 
  print("You typed an invalid number, you lose!") 
elif int(your_selection) == 0 and computer_choose == 2:
  print("You win!")
elif computer_choose == 0 and int(your_selection) == 2:
  print("You lose")
elif computer_choose > int(your_selection):
  print("You lose")
elif int(your_selection) > computer_choose:
  print("You win!")
elif computer_choose == int(your_selection):
  print("It's a draw")
