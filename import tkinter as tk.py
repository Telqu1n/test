import tkinter as tk


def get_customer_details():
    # Function to get customer details (name, address, phone number)
    name = name_entry.get()
    address = address_entry.get()
    phone_number = phone_entry.get()


    return {'name': name, 'address': address, 'phone_number': phone_number}


def get_number_of_cars():
    # Function to get the number of cars the customer wants to drive
    global NumCars
    NumCars = int(num_cars_entry.get())
    if NumCars > 5:
        print("You can only drive a maximum of 5 cars")


def get_car_choices():
    # Function to get the cars the customer wants to drive
    car_choice = [] # Initialise an empty list to store the car choices
 
    for i in range(NumCars):
        car_choice.append(car_choices_entry[i].get()) # Add the car choice to the list


    return car_choice # Return the list of car choices


def get_additional_laps():
    # Function to get the number of additional laps (if applicable)
    global AdditionalLaps
    AdditionalLapCheck = additional_laps_entry.get().title()
    if AdditionalLapCheck == "Yes":
        AdditionalLaps = int(additional_laps_num_entry.get())
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
    for car_choice in car_choices:
        if car_choice == "Lamborghini Gallardo":
            TotalCarCost += 59
        elif car_choice == "Lamborghini Huracan":
            TotalCarCost += 59
        elif car_choice == "Ferrari F40":
            TotalCarCost += 49
        elif car_choice == "Porsche Boxster":
            TotalCarCost += 39
        elif car_choice == "Audi A5":
            TotalCarCost += 39
        elif car_choice == "BMW i8":
            TotalCarCost += 39
        elif car_choice == "Lotus Elise":
            TotalCarCost += 30
    TotalLapCost = AdditionalLaps * 15
    TotalCost = TotalCarCost + TotalLapCost


def generate_bill(customer_details, number_of_cars, car_choices, additional_laps, total_cost):
    # Function to generate the bill with all the details
    bill_text.delete(1.0, tk.END) # Clear the bill text widget
    bill_text.insert(tk.END, "----- Bill -----\n\n")
    bill_text.insert(tk.END, "Customer Details:\n")
    bill_text.insert(tk.END, f"Name: {customer_details['name']}\n")
    bill_text.insert(tk.END, f"Address: {customer_details['address']}\n")
    bill_text.insert(tk.END, f"Phone Number: {customer_details['phone_number']}\n\n")
    bill_text.insert(tk.END, "Car Choices:\n")
    for i, car_choice in enumerate(car_choices):
        bill_text.insert(tk.END, f"Car {i+1}: {car_choice}\n")
    bill_text.insert(tk.END, f"\nAdditional Laps: {additional_laps}\n\n")
    bill_text.insert(tk.END, "Breakdown of Costs:\n")
    bill_text.insert(tk.END, f"Car Cost: {TotalCarCost}\n")
    bill_text.insert(tk.END, f"Additional Lap Cost: {TotalLapCost}\n\n")
    bill_text.insert(tk.END, f"Total Cost: {TotalCost}\n")


def main():
    # Main function to orchestrate the program flow
    customer_details = get_customer_details()
    number_of_cars = get_number_of_cars()
    car_choices = get_car_choices()
    additional_laps = get_additional_laps()
    calculate_cost(number_of_cars, car_choices, additional_laps)
    generate_bill(customer_details, number_of_cars, car_choices, additional_laps, TotalCost)


# Create the main window
window = tk.Tk()
window.title("Car Rental System")


# Create labels and entry fields for customer details
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()


address_label = tk.Label(window, text="Address:")
address_label.pack()
address_entry = tk.Entry(window)
address_entry.pack()


phone_label = tk.Label(window, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(window)
phone_entry.pack()


# Create labels and entry fields for number of cars
num_cars_label = tk.Label(window, text="Number of Cars (Maximum of 5):")
num_cars_label.pack()
num_cars_entry = tk.Entry(window)
num_cars_entry.pack()


# Create labels and entry fields for car choices
car_choices_label = tk.Label(window, text="""Car Choices:
Lamborghini Gallardo
Lamborghini Huracan
Ferrari F40
Porsche Boxster
Audi A5
BMW i8
Lotus Elise""")


car_choices_label.pack()
car_choices_entry = []
for i in range(5):
    car_choice_entry = tk.Entry(window)
    car_choice_entry.pack()
    car_choices_entry.append(car_choice_entry)


# Create labels and entry fields for additional laps
additional_laps_label = tk.Label(window, text="Additional Laps (Yes/No):")
additional_laps_label.pack()
additional_laps_entry = tk.Entry(window)
additional_laps_entry.pack()


additional_laps_num_label = tk.Label(window, text="Number of Additional Laps:")
additional_laps_num_label.pack()
additional_laps_num_entry = tk.Entry(window)
additional_laps_num_entry.pack()


# Create a button to generate the bill
generate_bill_button = tk.Button(window, text="Generate Bill", command=main)
generate_bill_button.pack()


# Create a text widget to display the bill
bill_text = tk.Text(window, height=20, width=50)
bill_text.pack()


# Start the main event loop
window.mainloop()
