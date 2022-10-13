# Initialize a string you want to remove leading zeros
str_left = "000Learn Share IT00000"

# Remove leading and trailing zeros
new_str_1 = str_left.lstrip("0")
new_str_2 = new_str_1.rstrip("0")

# Print new string
print("New string remove leading and trailing zeros: ",new_str_2)