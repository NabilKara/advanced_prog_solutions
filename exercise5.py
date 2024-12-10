print("Runner 1:")
name_runner_one = input("Name: ")
try:
    time_runner_one = float(input("Time (in seconds) : "))
except ValueError:
    print("Time must be a decimal or integer number")
print("Runner 2:")
name_runner_two = input("Name: ")
try:
    time_runner_two= float(input("Time (in seconds) : "))
except ValueError:
    print("Time must be a decimal or integer number")
if(time_runner_one > time_runner_two):
    print(f"The faster runner is : {name_runner_one}")
elif(time_runner_one < time_runner_two):
    print(f"The faster runner is : {name_runner_two}")
else: 
    print(f"{name_runner_one} and {name_runner_two} have the same time")