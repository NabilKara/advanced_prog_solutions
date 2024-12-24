#  Returns the number of elements.
def length(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of numbers.")
    return len(lst)

# Calculates the arithmetic mean.
def mean(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of numbers.")
    Sum = sum(lst)
    try:
        return Sum / length(lst)
    except ZeroDivisionError: 
        print("Can't calculate mean of an empty list")
# Returns the difference between max and min values.
def range_of_list(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list of numbers.")
    if(length(lst) != 0):
        copy_list = lst[:]
        copy_list.sort()
        return copy_list[length(lst) - 1] - copy_list[0]
    else :
        return 0
# calculate standard deviation
def standard_deviation(data):
    if not isinstance(data, list):
        print("Input must be a list of numbers.")
        return
    n = len(data)
    if n < 2:
        print("Standard deviation requires at least two data points.")
        return
    
    Mean = mean(data)
    variance = sum((x - Mean) ** 2 for x in data) / (n - 1) 
    std_dev = variance ** 0.5  
    return std_dev
#test cases:
tc_1 = []
tc_2  = [-3,-2,-4,1,2,3]
tc_3 = [0.5,0.5,0.6,0.3]
tc_4 = [2]

print(f"Test case 1 : {tc_1}")
print(f"Test case 2 : {tc_2}")
print(f"Test case 3 : {tc_3}")
print(f"Test case 4 : {tc_4}")

print(f"length {length(tc_1)}")
print(f"mean {mean(tc_1)}")
print(f"range {range_of_list(tc_1)}")
print(f"standard deviation {standard_deviation(tc_1)}")


print(f"length {length(tc_2)}")
print(f"mean {mean(tc_2)}")
print(f"range {range_of_list(tc_2)}")
print(f"standard deviation {standard_deviation(tc_2)}")

print(f"length {length(tc_3)}")
print(f"mean {mean(tc_3)}")
print(f"range {range_of_list(tc_3)}")
print(f"standard deviation {standard_deviation(tc_3)}")

print(f"length {length(tc_4)}")
print(f"mean {mean(tc_4)}")
print(f"range {range_of_list(tc_4)}")
print(f"standard deviation {standard_deviation(tc_4)}")