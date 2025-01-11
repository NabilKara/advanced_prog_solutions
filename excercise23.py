try:
    input = int(input("Enter a positive integer: "))
except ValueError:
    print("Please enter a valid integer")
    exit()
if input < 0:
    print("Please enter a positive integer")
    exit()
else:
    for i in range(-input,input+1):
        print(i)