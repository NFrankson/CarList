import random

cars = []  # Move the list outside the loop

while True:
    cars.append(str(input("What car would you like to add?: ")))
    print("List of cars:", cars)
    
    for index, car in enumerate(cars):
        print(f"{index + 1}. {car}")

    # Ask the User if they would like to add more to the list
    addMore = input("Would you like to add more? (yes/no): ")

    # Ask the user if they would like to remove a car
    optToRemove = input("Would you like to remove a car? (yes/no): ")

    if optToRemove.lower() == "yes":
        # Ask the user which car to remove
        carToRemove = str(input("What car would you like to remove?: "))
        # Check if the car is in the list before removing it
        if carToRemove in cars:
            cars.remove(carToRemove)
            print(f"{carToRemove} removed.")
        else:
            print(f"{carToRemove} not found in the list.")
    
    if addMore.lower() != 'yes':
        print("Goodbye!")
        break

# Now you can use the 'cars' list outside the loop
print("Final list of cars:", cars)