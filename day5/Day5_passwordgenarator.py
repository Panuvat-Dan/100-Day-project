#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Method1
letter_total = ""
for letter in range(nr_letters):
  letter_total = letter_total + letter_total.join(random.choice(letters))


symbol_total = ""
for symbol in range(nr_symbols):
  symbol_total = symbol_total + symbol_total.join(random.choice(symbols))

number_total = ""
for number in range(nr_numbers):
  number_total = number_total + number_total.join(random.choice(numbers))

password_genarator = letter_total+symbol_total+number_total
print(password_genarator)

#Method2
char_total = ""
for char in range(nr_letters):
  char_total = char_total + random.choice(letters)

for char in range(nr_symbols):
  char_total = char_total + random.choice(symbols)

for char in range(nr_numbers):
  char_total = char_total + random.choice(numbers)

print(char_total)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Method1 random within oldpassword_list

hard_lvl_password = ""
for i in range(len(password_genarator)):
  hard_lvl_password = hard_lvl_password + hard_lvl_password.join(random.choice(password_genarator))
print(hard_lvl_password)

#Method2 random from global list above

password_list = []
for char in range(1,nr_letters+1):
  password_list.append(random.choice(letters))

for char in range(1,nr_symbols+1):
  password_list = password_list + random.choice(symbols)

for char in range(1,nr_numbers+1):
  password_list = password_list + random.choice(numbers)

print(random.shaffle(password_list))