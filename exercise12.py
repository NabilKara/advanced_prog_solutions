try:
    width= int(input("Width: "))
    height = int(input("Height: "))
except ValueError:
    print("Width must be an integer")
    exit()

for _ in range(height):
    for _ in range(width):
        print("#",end='')
    print(end=' ')