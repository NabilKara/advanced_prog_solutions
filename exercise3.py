try:
    amount = float(input("Total Amount: "))
except ValueError:
    print("Input must be a number")
try:
    nb_items = int(input("Number of items: "))
except ValueError:
    print("Input must be an integer")

days_of_week = ["Sunday","Saturday","Monday", "Tuesday", "Wednesday", "Thursday"]
day_week = input("Day of the week: ")
if day_week not in days_of_week :
    print("You must enter a full and valid day of the week")
    exit()
discount = 0.10 if day_week not in ["Saturday","Sunday"] else 0.20
discount += 0.5 if nb_items > 5 else 0
print(f"Total price after discount: { round(amount * (1- discount),2)} dinars")