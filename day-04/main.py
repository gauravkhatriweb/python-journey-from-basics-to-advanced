# Output
print("Welcome to the Age Classifier!")
# Input
user_input = int(input("Enter a Age: "))
# String formatting
print(f"You entered: {user_input}")


# Oprators
# = Assignment operator

age = user_input
# + Addition operator
age_next_year = age + 1
# - Subtraction operator
age_last_year = age - 1
# * Multiplication operator 
age_in_5_years = age * 5 
# / Division operator
age_half = age / 2
# % Modulus operator
age_mod_10 = age % 10
# ** Exponentiation operator
age_squared = age ** 2
# // Floor division operator
age_floor_div = age // 2
# Comparison operators
is_adult = age >= 18
is_senior = age >= 65
# Logical operators
is_teenager = age >= 13 and age < 20
is_child = age < 13
# Output results
print(f"Next year, you will be: {age_next_year}")
print(f"Last year, you were: {age_last_year}")
print(f"In 5 years, you will be: {age_in_5_years}")
print(f"Half of your age is: {age_half}")
print(f"Your age mod 10 is: {age_mod_10}")
print(f"Your age squared is: {age_squared}")
print(f"Your age floor divided by 2 is: {age_floor_div}")
print(f"Are you an adult? {is_adult}")
print(f"Are you a senior? {is_senior}")
print(f"Are you a teenager? {is_teenager}")
print(f"Are you a child? {is_child}")


