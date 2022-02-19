import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#for l in range(0,nr_letters+1):
    #print(letters[l])
pass_letter = ''
for l in range(0,nr_letters):
    pass_letter += random.choice(letters)
    #print(pass_letter)
#random letter in password

pass_symbol = ''
for s in range(0,nr_symbols):
    pass_symbol += random.choice(symbols)
#print(pass_symbol)

#random letter and symbol in password

pass_number = ''
for n in range(0,nr_numbers):
    pass_number += random.choice(numbers)
#print(pass_number)
password = pass_letter + pass_symbol + pass_number
#print(password.split())

password_letter = list(password)
#convert to a list
random.shuffle(password_letter)
#reorganize the list
finall_pass = ''
#change to a string
for char in password_letter:
    finall_pass += char
print(f"Your passwrod is: {finall_pass}")