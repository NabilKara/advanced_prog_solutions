numbers = [1,2,3,4,5]
index = 0
print("The initial list is : ")
print(numbers)
while(index != -1):
        try:
            index = int(input("Enter an index between 0 and 4 , enter -1 to exit: "))
        except ValueError:
            print("index must be an integer")
            exit()
        if(index > 4 or index < -1):
            print("index must be between 0 and 4 or -1 to exit")
            print("Enter another valid index (between 0 and 4)")
        if(index != -1):
            try:
                num = int(input("Enter an integer: "))
            except ValueError:
                print("number must be an integer")
                exit()
            try: 
                numbers[index] = num
            except IndexError:
                print("index out of bounds error")
            print("List after update: ")
            print(numbers)
print("you typed -1 , good bye !")