#Data Types
#In Python, there are several built-in data types that you can use to store different types
#of data. Some of the most common data types include:
#1. int: This data type is used to store whole numbers. Example:
age = 30
#2. float: This data type is used to store decimal numbers. Example:
height = 1.75
#3. str: This data type is used to store text. Example:
name = "Alice"
#4. bool: This data type is used to store boolean values (True or False).
is_student = True
#5. list: This data type is used to store a collection of items. Example:
fruits = ["apple", "banana", "cherry"]
#6. tuple: This data type is similar to a list, but it is immutable ( cannot be changed). Example:
coordinates = (10, 20)
#7. dict: This data type is used to store key-value pairs. Example:
person = {"name": "Alice", "age": 30, "height": 1.75}
#8. set: This data type is used to store a collection of unique items. Example
unique_numbers = {1, 2, 3, 4, 5}
#You can also use the type() function to check the data type of a variable. Example:
print(type(name)) #Output: <class 'str'>
print(type(age)) #Output: <class 'int'>
print(type(height)) #Output: <class 'float'>
print(type(is_student)) #Output: <class 'bool'>
print(type(fruits)) #Output: <class 'list'>
print(type(coordinates)) #Output: <class 'tuple'>
print(type(person)) #Output: <class 'dict'>
print(type(unique_numbers)) #Output: <class 'set'>

#Strings 
#A string is a sequence of characters enclosed in quotes. Example:
greeting = "Hello, World!"
#You can use single quotes, double quotes, or triple quotes to create a string. Example
name = 'Alice'
message = "It's a nice day!"
multiline_string = """This is a multi-line string.
It can span multiple lines."""
#You can also use the str() function to convert other data types to a string. Example
age = 30
age_str = str(age)
print(age_str) #Output: "30"    


#Type Conversion
#In Python, you can convert between different data types using built-in functions. Some of the
#most common type conversion functions include:
#1. int(): This function converts a value to an integer. Example:
age_str = "30"
age = int(age_str)
print(age) #Output: 30
#2. float(): This function converts a value to a float. Example:
height_str = "1.75"
height = float(height_str)
print(height) #Output: 1.75
#3. str(): This function converts a value to a string. Example:
age = 30
age_str = str(age)
print(age_str) #Output: "30"
#4. bool(): This function converts a value to a boolean. Example:
is_student_str = "True"
is_student = bool(is_student_str)
print(is_student) #Output: True
#5. list(): This function converts a value to a list. Example:
fruits_str = "apple,banana,cherry"
fruits = list(fruits_str.split(","))
print(fruits) #Output: ["apple", "banana", "cherry"]
#6. tuple(): This function converts a value to a tuple. Example:
coordinates_list = [10, 20]
coordinates = tuple(coordinates_list)
print(coordinates) #Output: (10, 20)
#7. dict(): This function converts a value to a dictionary. Example:
person_list = [("name", "Alice"), ("age", 30), ("height",
1.75)]
person = dict(person_list)
print(person) #Output: {"name": "Alice", "age": 30, "height": 1.75}
#8. set(): This function converts a value to a set
unique_numbers_list = [1, 2, 3, 4, 5]
unique_numbers = set(unique_numbers_list)
print(unique_numbers) #Output: {1, 2, 3, 4, 5}

# Indexing and Slicing
#In Python, you can access individual characters in a string using indexing. The index starts at
#0 for the first character, 1 for the second character, and so on. Example:
greeting = "Hello, World!"
first_character = greeting[0]
print(first_character) #Output: "H"
second_character = greeting[1]
print(second_character) #Output: "e"
#You can also use negative indexing to access characters from the end of the string. Example:
last_character = greeting[-1]
print(last_character) #Output: "!"
second_last_character = greeting[-2]
print(second_last_character) #Output: "d"
#You can also use slicing to access a range of characters in a string. Example:
substring = greeting[0:5]
print(substring) #Output: "Hello"
substring = greeting[7:12]
print(substring) #Output: "World"
#You can also omit the start or end index to slice from the beginning or to the end
substring = greeting[:5]
print(substring) #Output: "Hello"
substring = greeting[7:]
print(substring) #Output: "World!"


