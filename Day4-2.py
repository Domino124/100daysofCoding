# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#print(names)
import random

number = len(names)
random_choice = random.randint(0, number - 1)
person = names[random_choice]
print(person + " is going to buy the meal today")
