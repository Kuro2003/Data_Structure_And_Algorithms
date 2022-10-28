# remove \r\n from a string of strings
str = "\r Learn Share IT \r\n"

res = str.replace("\n","").replace("\r","")
print(res)  # Learn Share IT

# -------------------------------------

# remove \r\n from a list of  strings
# Initial a list contain strings
a = ['\r line 1\r\n', '\n line 2\r\n', '\r\n line 3\r\n']

res1 = [i.replace("\n","").replace("\r","") for i in a ]
print(res1) # ['line 1', 'line 2', 'line 3']

