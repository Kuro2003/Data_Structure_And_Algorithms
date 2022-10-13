# Initialize a variable store string
str = "0000Learn Share IT12300000"

# Remove leading zeros
while str[0] == "0":
    str = str[1:]

# Remove trailing zeros
while str[-1] == "0":
    str = str[:-1]

# Print new string
print("New string is:",str)
