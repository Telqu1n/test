def get_customer_details():
    # Function to get customer details (name, address, phone number)
    name = input("Enter your name: \n")
    address = input("Enter your address: \n")
    phone_number = int(input("Enter your phone number: \n"))


    return {'name': name, 'address': address, 'phone_number': phone_number}


def get_number_of_cars():
    # Function to get the number of cars the customer wants to drive
    global NumCars
    NumCars = int(input("Enter the number of cars you want to drive (Maximum of 5): \n"))
    if NumCars > 5:
        print("You can only drive a maximum of 5 cars")
    else:
        print("You have to select at least 1 car")

def get_car_choices():
    # Function to get the cars the customer wants to drive
    print("Choose from the following cars: \n")
    print("1. Lamborghini Gallardo ")
    print("2. Lamborghini Huracan ")
    print("3. Ferrari F40 ")
    print("4. Porsche Boxster ")
    print("5. Audi A5 ")
    print("6. BMW i8 ")
    print("7. Lotus Elise ")


    car_choice = [] #Initialise an empty list to store the car choices


    for i in range (NumCars):
        global CarChoice
        CarChoice = int(input("Enter the number of the car you want to drive: \n"))
        if CarChoice == 1:
            CarChoice = "Lamborghini Gallardo"
        elif CarChoice == 2:
            CarChoice = "Lamborghini Huracan"
        elif CarChoice == 3:
            CarChoice = "Ferrari F40"
        elif CarChoice == 4:
            CarChoice = "Porsche Boxster"
        elif CarChoice == 5:
            CarChoice = "Audi A5"
        elif CarChoice == 6:
            CarChoice = "BMW i8"
        elif CarChoice == 7:
            CarChoice = "Lotus Elise"
        else:
            print("Invalid input. Please enter a number between 1 and 7")
            continue #skip the rest of the loop iteration


        car_choice.append(CarChoice) #add the car choice to the list


    return car_choice #return the list of car choices


def get_additional_laps():
    # Function to get the number of additional laps (if applicable)


    global AdditionalLaps
    AdditionalLapCheck = input("Do you want any aditional laps (£15 per lap)? (Yes/no): \n").upper()
    if AdditionalLapCheck == "YES" or AdditionalLapCheck == "Y" or AdditionalLapCheck == "NO" or AdditionalLapCheck == "N":
        AdditionalLaps = int(input("Enter the number of additional laps: \n"))
    else:
        AdditionalLaps = 0


def calculate_cost(number_of_cars, car_choices, additional_laps):
    # Function to calculate the total cost based on the inputs
    global TotalCarCost
    global TotalLapCost
    global TotalCost
    TotalCarCost = 0
    TotalLapCost = 0
    TotalCost = 0
    for i in range (NumCars):
        if CarChoice == "Lamborghini Gallardo":
            TotalCarCost += 59
        elif CarChoice == "Lamborghini Huracan":
            TotalCarCost += 59
        elif CarChoice == "Ferrari F40":
            TotalCarCost += 49
        elif CarChoice == "Porsche Boxster":
            TotalCarCost += 39
        elif CarChoice == "Audi A5":
            TotalCarCost += 39
        elif CarChoice == "BMW i8":
            TotalCarCost += 39
        elif CarChoice == "Lotus Elise":
            TotalCarCost += 30
    for i in range (AdditionalLaps):
        TotalLapCost += 15
    TotalCost = TotalCarCost + TotalLapCost


def generate_bill(customer_details, number_of_cars, car_choices, additional_laps, total_cost):
    # Function to generate the bill with all the details
    print("----- Bill -----\n")
    print("Customer Details:")
    print("Name:", customer_details['name'])
    print("Address:", customer_details['address'])
    print("Phone Number:", customer_details['phone_number'])
    print("\nCar Choices:")
    for i, car_choice in enumerate(car_choices):
        print(f"Car {i+1}: {car_choice}")
    print("\nAdditional Laps:", additional_laps)
    print("\nBreakdown of Costs:")
    print("Car Cost:", TotalCarCost)
    print("Additional Lap Cost:", TotalLapCost)
    print("\nTotal Cost:", TotalCost)




def main():
    # Main function to orchestrate the program flow
    customer_details = get_customer_details()
    number_of_cars = get_number_of_cars()
    car_choices = get_car_choices()
    additional_laps = get_additional_laps()
    total_cost = calculate_cost(number_of_cars, car_choices, additional_laps)
    generate_bill(customer_details, number_of_cars, car_choices, additional_laps, total_cost)


if __name__ == "__main__":
    main()
