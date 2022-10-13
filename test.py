# Initialize a string you want to remove leading zeros
str_left = "000124421"

# Remove leading zeros
new_str_1 = str_left.lstrip("0")

# Print new string
print("New string remove leading zeros:",new_str_1)

# Initialize a string you want to remove trailing zeros
str_left = "959500000"

# Remove leading zeros
new_str_2 = str_left.rstrip("0")

# Print new string
print("New string remove trailing zeros:",new_str_2)