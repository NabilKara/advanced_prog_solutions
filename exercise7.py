try:
    year = int(input("Please type in a year: "))
except ValueError: 
    print("You must type a valid year")
    exit()
leap = False
if(year % 4 == 0) : 
    
    if(year % 100 == 0 ):
        leap = year % 400 == 0 
    else:
        leap = True
if(leap) : 
    print("This is a leap year")
else:
    print("This isn't a leap year")