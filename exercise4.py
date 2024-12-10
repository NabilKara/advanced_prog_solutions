try: 
    age_one= int(input("Please type in the age of the first person: "))
    age_two = int(input("Please type in the age of the second person: "))
except ValueError:
    print("Input must be an integer")
    exit()
if(age_one > age_two) : print(f"The older age is: {age_one}")
elif (age_one < age_two):  print(f"The older age is {age_two}")
else : print("Both people are the same age!") 