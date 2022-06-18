# This is an integer value
age = 25
print(age)
print(type(age)) # The datatype of the variable

print()

# This is a floating point value
bmi = 27.825
print(bmi)
print(type(bmi)) # The datatype of the variable

# A simple mathematical expression; resulting value will be an integer
result_1 = 45 * 12 - 56 * 8 + 2
print(result_1)

# A simple mathematical expression; the resulting value will be a decimal (because of the division operation)
result_2 = 45 * 12 - 56 / 8 + 2
print(result_2)

t1 = 20
t2 = -30
t3 = 100
t4 = 0.25
t5 = 0.001

# A mathematical expression from variables
expr_1 = ((t1 + t2 + t3) / (t4 * 25)) / t5
print(expr_1)

# Combining the results of expr_1 with previous variables
expr_2 = (expr_1 * result_1) / result_2
print(expr_2)

expr_a = 25 * 10 - 7 + 32
expr_b = 56 - 100 + 85

# Performing decimal division
result_decimal = expr_a / expr_b
print(result_decimal)

# Performing integer division
# This is a demonstration of pt. b from above
result_integer = expr_a // expr_b
print(result_integer)

# Floating point division (default expected behavior)
t = 5 / 3
print(t)

# Integer division
# Both LHS and RHS of // are integers; result will also be integer
t = 5 // 3
print(t)

# Floating point division
# Both LHS and RHS of / are decimals; result will be a floating point number
t = 5.5 / 3.2
print(t)

# Integer division
# LHS and RHS of // are decimals; result will be a floating point number with fractional part removed
t = 5.5 // 3.2
print(t)

# Integer division
# LHS is a floating point number; result will be a floating point number with fractional part removed
t = 5.5 // 3
print(t)

# Integer division
# RHS is a floating point number; result will be a floating point number with fractional part removed
t = 5 // 3.2
print(t)

result_decimal = expr_1 / expr_2
print(result_decimal)

# Both LHS (expr_1) and RHS (expr_2) do not evaluate to integer the result is decimal 
# But the fractional part is removed
# This is a demonstration of pt. a from above
result_integer = expr_1 // expr_2
print(result_integer)

number_1 = 56
number_2 = 8
number_3 = 5
number_4 = 12

print(number_1 % number_2) # output should be 0
print(number_1 % number_3) # output should be 1
print(number_1 % number_4) # output should be 8

t = (number_1 % number_4) % number_2 # output should be 0
print(t)

t = (number_1 % number_4) % number_3 # output should be 3
print(t)

t = number_3 % number_2 # if x < y for x % y then the result is always x
print(t)

# Two raised to 5; result is 32
print(2 ** 5)

# 5 raised to 2; result is 125
print(5 ** 3)

a = 5

# Convert the int to binary
b = bin(a)

# Convert the binary back to int
# To convert back to decimal integer, we also need to specify the base (in this case 2)
i = int(b, 2)

print("binary: ", b)
print("integer:", i)

a = 200
print('value:', a)
print('address:', id(a)) # Current memory location of variable 'a'

print() # Print an empty line for better output representation

a = a * 10 # 200 * 10 = 2000
print('value:', a)
print('address:', id(a)) 

print()

a = a / 5 # 2000 / 5 = 400.0
print('value:', a)
print('address:', id(a))

print()

a = a - 10 * a / 1000 # 400.0 - 10 * 400.0 / 1000 = 400.0 - 10 * 0.4 = 400.0 - 4.0 = 396.0
print('value:', a)
print('address:', id(a))

a = 10
a /= 2
print(a)

a = 20
a *= 5
print(a)