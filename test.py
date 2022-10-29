import thread

def print_rectangular(num1,num2,num3):
    print("Cube: {}" .format(num1 * num2 * num3))

def print_rectangle(num1,num2):
    # function to print square of given num
    print("Square: {}" .format(num1 * num2))

if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_rectangle, args=(10,20))
    t2 = threading.Thread(target=print_rectangular, args=(10,20,30))

    # starting thread
    t1.start()
    t2.start()

    # wait thread is executed successful
    t1.join()
    t2.join()

    # thread executed cuccessful
    print("Done!") 