def read_numbers_from_file(filename):
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                numbers.extend(int(num) for num in line.split())
        return numbers
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. continuing with default")
    except ValueError:
        print(f"Error: The file contains non-numeric data. continuing with default")
    except Exception as e:
        print(f"An unexpected error occurred: {e}, continuing with default")
    return [1,2,3,4,5]

def write_numbers_to_file(numbers, filename):
    try:
        with open(filename, 'w') as file:
            file.write(' '.join(map(str, numbers)) + '\n')
        print(f"Successfully wrote numbers to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


def main():
    numbers = read_numbers_from_file(input("Enter a file path: "))
    while(True):
        print(f"Numbers list {numbers}")
        choice = 0
        print("Here's a list of options that you can choose from")
        print("1 append")
        print("2 Insert")
        print("3 Pop")
        print("4 remove")
        print("5 sorting")
        print("6 reversing")
        print("7 store list in a file")
        print("8 quit")
        try:
            choice = int(input("Enter your choice: "))
            if(choice == 1):
                value  = int(input("Enter a value to append to the list: "))
                numbers.append(value)
            elif(choice == 2):
                value  = int(input("Enter a value to insert into the list: "))
                index = int(input(f"Enter a valid index between 0 and {len(numbers) - 1}: "))   
                numbers[index] = value
            elif(choice == 3):
                numbers.pop()
            elif(choice == 4):
                value  = int(input("Enter a value to delete from the list: "))
                numbers.remove(value)
            elif (choice == 5): 
                numbers.sort()
            elif (choice == 6):
                numbers.reverse()
            elif (choice == 7):
                filename  = input("Enter a filename to write the list in: ")
                write_numbers_to_file(numbers,filename)
            elif(choice == 8):
                print("Good bye !!")
                exit()
            else:
                print("We were not able to determine your choice , please try again")
        except IndexError:
            print("Index out of bounds or empty list error")
        except ValueError:
            print("Choice must be an integer, Operation denied")
if __name__ == "__main__":
    main()