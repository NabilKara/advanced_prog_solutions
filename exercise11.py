try:
    width= int(input("Width: "))
except ValueError:
    print("Width must be an integer")
    exit()

for i in range(width):
    print("#",end='')