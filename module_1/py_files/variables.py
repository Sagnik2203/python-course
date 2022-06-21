# Python variables names with multiple words are separated by underscore character "_" 
# This style is called snake-case
# Variables which change values are denoted with small case characters
var = True
some_variable = 20
another_variable = "hello world"

print(var)
print(some_variable)
print(another_variable)

# Values inside variables can be updated anytime we want
var = False
some_variable = "New Value"
another_variable = 67.88

print(var)
print(some_variable)
print(another_variable)

# Variables which do not change their value during the course of execution are denoted with capital case characters
PI = 3.141
H = 6.626 * 10e-34

print(PI)
print(H)

# Variables denoted as constants can also be updated dynamically
PI = 5.6666
H = 2000

print(PI)
print(H)

# Variable multi definition
# Define multiple variables simultaneously
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Binding more or less number of values to the variables leads to error
# a, b, c = 10, 20
# x, y, z = 100, 200, 300, 400

# Data of type 'str'
print(type("hello"))

# Data of type 'int'
print(type(23))

# Data of type 'float'
print(type(56.23))

# Data of type 'bool'
print(type(False))

# Data of type 'list'
print(type([]))

# Data of type 'dict'
print(type({}))

a = 4
b = 4
c = "string"
d = 45.0
e = "string"
f = 45.0

print("a:", a)
print("id(a)", id(a))
print()

print("b:", b) 
print("id(b)", id(b))
print()

print("c:", c)
print("id(c)", id(c))
print()


print("d:", d)
print("id(d)", id(d))
print()

print("e:", e)
print("id(e)", id(e))
print()

print("f:", f)
print("id(f)", id(f))
print()