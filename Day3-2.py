# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height**2)
#print(f"Your BMI is: {BMI:.0f}")
if BMI > 35:
  print(f"Your BMI is: {BMI:.0f}, you are clinically obese")
elif BMI < 18.5:
    print(f"Your BMI is {BMI:.0f}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI:.0f}, you are normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI:.0f}, you are slightly overweight")
else: 
    print(f"Your BMI is {BMI:.0f}, you are obese")
  

