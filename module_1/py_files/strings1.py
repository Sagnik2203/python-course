# Single quoted string
string_1 = '[1]. hello world'
print(string_1)

# Double quoted string
string_2 = "[2]. hello world again!"
print(string_2)

# Multi line string
string_3 = '''[3]. This is a multi line string
that is spread over many lines, this being the second line
but definitely not the last there will also be one more line.
This is the last line of the multi-line string'''
print(string_3)

# To check for the type 
print(type(string_1))

B = "hello"
C = "world"

# Concatenate string C to string B
A = B + C
print(A)

# Concatenate string B to string C
A = C + B
print(A)

# String can be concatenated with a number that is represented as a string
my_string = "hello" + " " + "world" + " " + "101"
print(my_string)

# Numbers represented as strings get concatenated
my_string = "101" + "10"
print(my_string)

# String CANNOT be concatenated with a number that is NOT represented as a string
# This will result in a runtime error
my_string = "hello" + " " + "world" + " " + 101
print(my_string)

my_string = "hello" + " " + str(125)
print(my_string)

my_string = str(101) + str(919)
print(my_string)

# Integer type conversion
my_number = int(my_string)
my_number *= 100
print('number:', my_number)

# Type conversion from number to float
my_float = float(my_number)
print('float:', my_float)

print()

d1 = 23.989
d2 = 23.125

# Type conversion from float to number
print('number:', int(d1))
print('number:', int(d2))

my_string = "hello " * 3
print(my_string)

my_string = (("A" * 5) + " ") * 3
print(my_string)

# Check the length of the string
my_string = "help"
print(my_string)
print(len(my_string))

print()

# Update the current string; length will also get updated
my_string = my_string + "ME!"
print(my_string)
print(len(my_string))

# The escape sequence \ tells python to consider the following character as a string
string = 'today is teacher\'s day'
print(string)

# The escape sequence \n tells Python to print a newline immediately after
string = 'hello\nworld'
print(string)

# The escape sequence \t tells Python to print a tab immediately after
string = '\thello\tworld'
print(string)

name = "Bob"

# Creating a simple f-string using a variable
greeting = f"Hello, {name}"
print(greeting)

# Updating the variable does not update the original f-string
name = "David"
print(greeting)

# F-string works with numbers without type conversion
age = 23
message = f"Bob is {age} years old"
print(message)

name = "Eugene"

# Creating a template string
template = "How are you {}?"
message_1 = template.format(name)

# Creating a new string by updating the variable used in the template string
name = "Max"
message_2 = template.format(name)

print(message_1)
print(message_2)

message_title = "Charles"
message_body = "Hello there"
message_footer = "Good day to you!"

# A formatted string using multiple variables
template = "{} {}, {}"

# Creating the first string from template
message_1 = template.format(message_body, message_title, message_footer)

message_title = "Joseph"
message_body = "Good evening"
message_footer = "Welcome Back!"

# Updating the variables and creating a new string from template
message_2 = template.format(message_body, message_title, message_footer)

print(message_1)
print(message_2)

# If variable names are not specified in the template, the order is important
template = "Hello {} {}"

# Printing in the order in which the values are provided
message_1 = template.format("Anish", "Pal")
message_2 = template.format("Pal", "Anish")

print(message_1)
print(message_2)

# Formatted string using format() and variable names
template = "Hello {first_name} {last_name}"
greeting_1 = template.format(first_name="Anish", last_name="Pal")
print(greeting_1)

greeting_2 = template.format(first_name="John", last_name="Doe")
print(greeting_2)

# Using this approach the order of variables in template does not matter 
greeting_3 = template.format(last_name="Beckham", first_name="David")
print(greeting_3)

# Template strings
inner_template = "inside inner template {}"
outer_template = "INSIDE OUTER TEMPLATE {} {}"

# Create a string using nested template strings
buffer_1 = outer_template.format(inner_template.format("<INNER>"), "<OUTER>")
buffer_2 = outer_template.format("<OUTER>", inner_template.format("<INNER>"))

print(buffer_1)
print(buffer_2)

# Template string with named variables
template = "Hi there, I am {name}, from {country} and I am {age} years old"

# Create the string from the template
message = template.format(name="Anish", country="India", age=28)
print(message)

number = 13
print(f"The square of {number} is {number ** 2}")
print("The cube of {} is {}".format(number, number ** 3))