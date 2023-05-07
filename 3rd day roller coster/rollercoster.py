#Day 3 Python

#print("Welcome to the rollercoster!")
#height = int(input("Please enter your height in cm: "))
#age =  int(input("Please enter your age: "))
#if (120<=height<300) and (18<= age <= 100):
#  print("You are eligible to enter ")
#  if age >= 18:
#    print("you need to pay 20$ ")
#  elif age < 18:
#    print("You need to pay 13$ ")
#elif height >= 300 and age >=101:
#  print(f"Man, are you HULK? Are you fucking kidding me? And You are not {age} years old kurwaaaa")
#  if age >= 18:
#    print("you need to pay 20$ ")
#  elif age < 18:
#    print("You need to pay 13$ ")
#else:
#  print("You are not eligible ")

#Second Project
#number = int(input("which number do you want to check?"))
#if number % 2 == 0 :
#  print("the number is even")
#else:
#  print("The number is odd")

# Third project
#print("Welcome to the second rollercoster ")
#height = int(input("Enter your height in cm please! "))
#age = int(input("Please enter your age "))
#if height > 120 and age>18:
#  print("You are eligible to enterr")
#else:
#  print ("You are not eligible to enter")

#1.1 Project
print("welcome to the Aqua park!")
height = int(input("Please enter your height in cm!"))
bill = 0
if height >= 120:
  print("You are allowed to enter")
  age = int(input("Please enter your age!"))
  if age >= 18 and age < 45:
    print("You need to pay 25$ ")
    bill = 25
  elif age >= 55 and age <= 65:
    print("You have a free ride")
    bill = 0
  elif age > 300:
    print("WTF man Are you HULK?")
    bill += 25
  else:
    print("You need to pay 20$ ")
    bill = 20
  photo = input("Do you want to take photo? If Yes press 'Y' if no 'N'y\n")
  if photo == "Y":
    if age >= 55 and age <= 65:
      bill = 0
    else:
      bill = bill + 3
  if photo == "N":
    bill == 0

else:
  print("You are not allowed to enter! ")
print(f"Your final bill is {bill}$")
# 🚨 Don't change the code below 👇
#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆
#bmi = weight / (height**2)
#bmi = round(bmi, 1)
#if bmi <= 18.5:
#  print(f"Your BMI is {bmi}, you are underweight.")
#elif bmi >= 18.5 and bmi <= 25:
#  print(f"Your BMI is {bmi}, you have a normal weight!.")
#elif bmi >= 25 and bmi <= 30:
#  print(f"Your BMI is {bmi}, you are obese.")
#else:
#  print(f"Your BMI is {bmi}, you are clinically obese.")
