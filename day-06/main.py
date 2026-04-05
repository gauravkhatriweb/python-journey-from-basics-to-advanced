#Loops
#Loops is a programming structure that repeats a sequence of instructions until a specific condition is met.
#There are two main types of loops in Python: for loops and while loops.
#For loops are used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
#While loops are used to repeat a block of code as long as a certain condition is true
#For loop example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#While loop example
count = 0
while count < 5:
    print(count)
    count += 1
#Nested loops are loops inside loops. They are used to iterate over multi-dimensional data structures, such as lists of lists.
#Nested loop example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element)  
#Loop control statements are used to alter the flow of a loop. They include break, continue, and pass.
#Break statement example
for i in range(10):
    if i == 5:
        break
    print(i)
#Continue statement example
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#Pass statement example 
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)    


# These are list of question name then one by one and solve them using loops 
#Q1: Accept an integer and Print hello world n times
a = int(input("Enter an integer: "))
for i in range(a):
    print("Hello World")





#Q2: Print natural number up to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

#Q3: Reverse for loop. Print n to 1
for i in range(n, 0, -1):
    print(i)

#Q4: Take a number as input and print its table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#Q5: Sum up to n terms
n = int(input("Enter a number: "))
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"The sum of the first {n} natural numbers is: {total_sum}")

#Q6: Factorial of a number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")

#Q7: Print the sum of all even & odd numbers in a range separately
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
even_sum = 0
odd_sum = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"The sum of even numbers in the range is: {even_sum}")
print(f"The sum of odd numbers in the range is: {odd_sum}")

#Q8: Print all the factors of a number
num = int(input("Enter a number: "))
print(f"The factors of {num} are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

#Q9: Accept a number and check if it a perfect number or not.
# A number whose sum of factors is equal to the number itself
# Ex - 6 = 1, 2, 3 = 
num = int(input("Enter a number: "))
factor_sum = 0
for i in range(1, num):
    if num % i == 0:
        factor_sum += i
if factor_sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

#Q10: Check wether the number is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#Q11: Reverse a string without using in build functions.
input_string = input("Enter a string: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
print(f"The reversed string is: {reversed_string}")

#Q12: Check string is Pallindrome or not
input_string = input("Enter a string: ")
reversed_string = ""
for char in input_string:
    reversed_string = char + reversed_string
if input_string == reversed_string:
    print(f"{input_string} is a palindrome.")

#Q13: Count all letters, digits, and special symbols from a given
# string
# Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4 
str1 = "P@#yn26at^&i5ve"
char_count = 0
digit_count = 0
symbol_count = 0
for char in str1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
print(f"Chars = {char_count}")
print(f"Digits = {digit_count}")
print(f"Symbols = {symbol_count}")


#While Loop
#The while loop repeats a block of code as long as a condition is True. It is useful when the number of iterations is unknown before execution
# While loop questions
#Q1: Separate each digit of a number and print it on the new line
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit)
    num //= 10

#Q2: Accept a number and print its reverse
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print(f"The reversed number is: {reversed_num}")

#Q3: Accept a number and check if it is a pallindromic number (If number and its reverse are equal?
num = int(input("Enter a number: "))
reversed_num = 0
temp = num
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if num == reversed_num:
    print(f"{num} is a palindromic number.")
else:
    print(f"{num} is not a palindromic number.")

#Q4: Create a random number guessing game with python.
import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break


    