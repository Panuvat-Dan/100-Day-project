alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
  new_text = ""
  for i in range(len(text)):
      char_position = alphabet.index(text[i])
      if direction == 'encode':
          new_text = new_text + new_text.join(alphabet[char_position+shift])
      elif direction == 'decode':
          text[i] = alphabet[char_position-shift]
          new_text = new_text + new_text.join(alphabet[char_position-shift])
  print(new_text)
  
    #Reference to call index from list
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text,shift)