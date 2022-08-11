def aa():
    global a 
    a = 10
    def bb():
        global a 
        a = 30
a = 12
aa()
print(a)