# FILEPATH: main.py

# Function to get customer details
def get_customer_details():
    name = input("Enter customer's name: ")
    address = input("Enter customer's address: ")
    phone_number = input("Enter customer's phone number: ")
    return name, address, phone_number

# Function to get car choices
def get_car_choices():
    num_cars = int(input("Enter the number of cars the customer would like to drive (maximum 5): "))
    cars = []
    for i in range(num_cars):
        car = input(f"Enter the car choice {i+1}: ")
        cars.append(car)
    return cars

# Function to get additional laps
def get_additional_laps():
    num_laps = int(input("Enter the number of additional laps (if required): "))
    return num_laps

# Function to calculate total cost
def calculate_total_cost(num_cars, num_laps):
    car_cost = num_cars * 100  # Assuming each car costs $100
    lap_cost = num_laps * 50  # Assuming each lap costs $50
    total_cost = car_cost + lap_cost
    return total_cost

# Function to generate bill
def generate_bill():
    name, address, phone_number = get_customer_details()
    cars = get_car_choices()
    num_laps = get_additional_laps()
    total_cost = calculate_total_cost(len(cars), num_laps)

    # Print the bill
    print("----- Bill -----")
    print("Customer Details:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone Number: {phone_number}")
    print("\nCar Choices:")
    for i, car in enumerate(cars):
        print(f"Car {i+1}: {car}")
    print("\nAdditional Laps:")
    print(f"Number of Laps: {num_laps}")
    print("\nCost Breakdown:")
    print(f"Car Cost: ${len(cars) * 100}")
    print(f"Lap Cost: ${num_laps * 50}")
    print("\nTotal Cost: $" + str(total_cost))

# Generate the bill
generate_bill()
