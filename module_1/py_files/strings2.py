string = "hello world"

# Index the first character
print(f'string[0]: {string[0]}')

# Index the second character
print(f'string[1]: {string[1]}')

# Index the 5th character
print(f'string[4]: {string[4]}')

# Index the last character
print(f'string[10]: {string[10]}')

# Index the last character by calculating
print(f"string[10]: {string[len(string) - 1]}")

string = "python"

print(f"{string[0]} -> {id(string[0])}")
print(f"{string[1]} -> {id(string[1])}")
print(f"{string[2]} -> {id(string[2])}")
print(f"{string[3]} -> {id(string[3])}")
print(f"{string[4]} -> {id(string[4])}")
print(f"{string[5]} -> {id(string[5])}")

string = "$12345"

# Print the last index using reverse index
print(f"string[-1]: {string[-1]}")

# Print the 3rd index using reverse index
print(f"string[-3]: {string[-3]}")

# Print the 1st index using reverse index
print(f"string[-6]: {string[-6]}")

# Print the 1st index using reverse index by calcuating
print(f"string[-6]: {string[-len(string)]}")

string = "01234567"

# Slice the first 4 characters of the string
print(f"string[0:3]: {string[0:4]}")

# Slice from the 4th character to the end of the string
print(f"string[3:6]: {string[3:7]}")

# Slice using reverse indexing from 4th character to end of string
print(f"string[3:6]: {string[-5:-1]}")

string = "0123456789"

# Slice from 4th index onwards
print(f"string[4:]\t{string[4:]}")

# Slice upto the 4th index
print(f"string[:4]\t{string[:4]}")

# Slice the whole string
print(f"string[:]\t{string[:]}")

string = "0123456789 ABCDEFGHIJ"
print(string)
print()

# Slice with a step of 3 in the range [2,12]
print(f"string[2:12:3]\n{string[2:12:3]}")
print()

# Slice with a step of 5 in the range[:]
print(f"string[::5]\n{string[::5]}")
print()

# Reverse a string 
print(f"string[::-1]\n{string[::-1]}")
print()

# Print from index -10 to index -1 in reverse 
print(f"string[-1:-10:-1]\n{string[-1:-11:-1]}")
print()

# Print from index -10 to index -1 in forward 
print(f"string[-10:-1]\n{string[-10:]}")
print()

string = "python"
print(f"{string} -> {id(string)}")

# This modification is allowed as it does not mutate the existing string
string = "pyThon"
print(f"{string} -> {id(string)}")

# This modification is allowed as it does not mutate the existing string
string = string + "."
print(f"{string} -> {id(string)}")

# This modification is not allowed as it mutates the existing string
# This will lead to an error
my_string = "python"
my_string[0] = "P"
print(my_string)

string_1 = "THE QUICK BROWN FOX"
string_2 = "jumps over the lazy dog"
string_3 = 2.355

print(f"{string_1}.isupper ? {string_1.isupper()}\n")
print(f"{string_1}.lower ? {string_1.lower()}\n")
print(f"{string_2}.upper ? {string_2.upper()}\n")
print(f"{string_3} with a precision of 5 ? {format(string_3, f'0.5f')}")

string = "the quick brown fox jumps over the lazy dog"
print(id(string))
print()

# New address of the string variable after replace()
string = string.replace("fox", "bear")
print(id(string))
print()

# New address of string variable after upper()
string = string.upper()
print(id(string))
print()

string = "python programming"
print(f"before modification -> ", string)
print()

# The result of replace() is not assigned to a variable
# After executing print function, the changes will not be accessible
print(string.replace("python", "javascript"))
print(f"after modification -> {string}")

