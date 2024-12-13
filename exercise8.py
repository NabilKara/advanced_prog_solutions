try:
    num= int(input("Number: "))
except ValueError: 
    print("Must enter an integer")
    exit()
output = ""
if(num % 3 == 0) :
    output += "Fizz"
if(num % 5 == 0) :
    output += "Buzz"
print("Output:")
print(output)
