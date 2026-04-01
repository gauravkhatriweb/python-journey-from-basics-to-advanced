# Condational Statements
# if, elif, else
# if condition:
#     # code to execute if condition is true
# elif another_condition:
#     # code to execute if another_condition is true
# else:
#     # code to execute if all conditions are false
# Example 1: Check if a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
# Example 2: Check if a person is eligible to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Example 3: Check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# Example 4: Check if a character is a vowel or consonant
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
elif char.isalpha():
    print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")


# Normal Practice: (My own code)
user_input = int(input("Enter a number: "))
if user_input > 10:
    print("Buy Ice Cream! ;)")
else:
    print("Get more Money :(")

# SOME QUESTIONS ON CONDITIONAL STATEMENTS:
#Q1: Accept two numbers and print the greatest between them. 
num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number:"))


if num1 > num2:
    print(f'{num1} is greater than {num2}')
elif num2 > num1:
    print(f'{num2} is greater than {num1}')
else:
    print("Both numbers are equal.")

#Q2: Accept the gender from the user and print the respective greeting message.
gender = input("Enter your gender (male or female): ").lower()
if gender == "male":
    print("Hello, Sir!")
elif gender == "female":
    print("Hello, Ma'am!")
else:
    print(f"Hello! {gender}!")  

#Q3: Accept an interger and check whether it is an even number or odd number.
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:   print(f"{number} is an odd number.")

#Q4: Aceept name and age from the user.Check whether the person is eligible to vote or not.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"{name}, you are eligible to vote.")
else:
    print(f"{name}, you are not eligible to vote.")


#Q5: Accept a year and check whether it is a leap year or not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Q6: Create if elif ladder using multiple conditions.
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
