# Greeting users
print("Welcome to the tip calculator")

individual_pay = 0
while individual_pay >= 0 :
  # to ask user the total bill 
  total_bill = input("What was the total bill?: ")

  # to ask percentage tip
  percentage_tip = input("What was your tip would you like to give? 10 or 12 or 15%: ")

  # to ask the number of people sharing
  number_sharing = input("How many people to split the bill: ")

  # calulating the bill for each
  total_bill_integer = int(total_bill)
  percentage_tip_interger = int(percentage_tip)
  number_sharing_interger = int(number_sharing)

  individual_pay = (total_bill_integer * 1+(percentage_tip_interger/100)) / number_sharing_interger
  print(f"Each person should pay {individual_pay} $.")


