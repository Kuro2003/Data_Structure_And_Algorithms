# Initialize a variable store string
from re import S


str = "0000Learn Share IT12300000"

# Remove leading zeros
while str[0] == "0":
    str = str[1:]

# Remove trailing zeros
while str[-1] == "0":
    str = str[:-1]

print("New string is:",str)
