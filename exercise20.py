def write_list_to_file(list, filename):
    try:
        with open(filename, 'w') as file:
            file.write(' '.join(map(str, list)) + '\n')
        print(f"Successfully wrote user  list to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


user_list = []
while(True):
    try:
        number= int(input("Enter a number [0 to exit]: "))
        if(number != 0):
            user_list.append(number)
            print(f"Current list: {user_list}")
            asc_list = user_list[:]
            asc_list.sort()
            desc_list = user_list[:]
            desc_list.sort(reverse=True)
            print(f"Sorted list in ascending order {asc_list}")
            print(f"Sorted list in descending order {desc_list}")
        else:
            print("Finished looping")
            break
    except ValueError:
        print("input must be an integer")
Sum = sum(user_list)
mean = Sum / len(user_list)
print(f"Mean : {mean}")
if(len(user_list) % 2 == 1) :
    print(f"Median is: {asc_list[int((len(user_list) -1) / 2) ]}")
else : 
    print(f"Median is: {(asc_list[int((len(user_list) -1) / 2) ] + asc_list[int(((len(user_list) - 1)) / 2) + 1]) / 2}")
decision = input("Do you want to save the user list to a file : [y/n]")
if(decision.lower() == "y"):
    filename = input("Enter a file path : ")
    write_list_to_file(user_list,filename)