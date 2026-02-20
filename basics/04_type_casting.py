# -------------------------------
# Implicit Type Casting
# -------------------------------


num_int = 10  # This is an integer
num_float = 3.14  # This is a floating-point number

result = num_int + num_float  # The integer is implicitly converted to a float before addition
print("Implicit Type Casting Example:")
print(f"Type of result: {type(result)}\n")
print(f"The result of adding {num_int} and {num_float} is: {result} and its type is: {type(result)}")  
# Output: 13.14 and <class 'float'>

# -------------------------------
# Explicit Type Casting
# -------------------------------


# Explicitly converting a string to an integer
string_number = "123"
converted_int = int(string_number)  # Explicitly converting the string to an integer
print("Explicit Type Casting Example:")

print(f"The original string is: '{string_number}' and its type is: {type(string_number)}")
print(f"The converted integer is: {converted_int} and its type is: {type(converted_int)}")


# Explicitly converting a integer to float
integer_number = 42
converted_float = float(integer_number)  # Explicitly converting the integer to a float
print(f"The original integer is: {integer_number} and its type is: {type(integer_number)}")
print(f"The converted float is: {converted_float} and its type is: {type(converted_float)}")

# Explicitly converting a float to an integer
float_number = 3.99
converted_int_from_float = int(float_number)  # Explicitly converting the float to an integer (truncates the decimal part)
print(f"The original float is: {float_number} and its type is: {type(float_number)}")
print(f"The converted integer from float is: {converted_int_from_float} and its type is: {type(converted_int_from_float)}")

# Explicitly converting a number to a string
number = 100
converted_string = str(number)  # Explicitly converting the number to a string
print(f"The original number is: {number} and its type is: {type(number)}")
print(f"The converted string is: '{converted_string}' and its type is: {type(converted_string)}")

# Explicitly converting a boolean to an integer
boolean_value = True
converted_int_from_bool = int(boolean_value)  # Explicitly converting the boolean to an integer (True becomes 1, False becomes 0)
print(f"The original boolean value is: {boolean_value} and its type is: {type(boolean_value)}")
print(f"The converted integer from boolean is: {converted_int_from_bool} and its type is: {type(converted_int_from_bool)}")

# -------------------------------
# Boolean Conversion
# -------------------------------

print("Boolean Conversion Examples:")
print(f"True as integer: {int(True)}")
print(f"False as integer: {int(False)}")
print(f"0 as boolean: {bool(0)}")
print(f"1 as boolean: {bool(1)}")
print(f"123 as boolean: {bool(123)}")

# -------------------------------
# Special Cases in Type Casting
# -------------------------------

# Explicitly converting a non-numeric string to an integer will raise a ValueError

# int("abc")      # ❌ Invalid
# int("10a")      # ❌ Invalid


# Explicitly converting a non-numeric string to a float will also raise a ValueError

# float("abc")    # ❌ Invalid
# float("3.14a")  # ❌ Invalid

# int("1.05")    # ❌ Invalid, cannot convert a float string directly to an integer without 
# first converting to float
# int(float("1.05"))  # This will convert the string "1.05" to a float and then to an integer, resulting in 1

