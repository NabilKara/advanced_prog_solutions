try :
    nb_people = int(input("How many people need a ride? "))
    nb_fit_taxi = int(input("How many people fit in one taxi? "))
except ValueError: 
    print("The input must be an integer")
    exit()
print(f"Number of taxis needed is {nb_people // nb_fit_taxi if nb_people % nb_fit_taxi == 0 else nb_people // nb_fit_taxi + 1 } ")