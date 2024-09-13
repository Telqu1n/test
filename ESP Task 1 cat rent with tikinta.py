import tkinter as tk

class CarRentalGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Car Rental")
        
        self.name_label = tk.Label(self.window, text="Enter your name:")
        self.name_entry = tk.Entry(self.window)
        self.name_label.pack()
        self.name_entry.pack()
        
        self.address_label = tk.Label(self.window, text="Enter your address:")
        self.address_entry = tk.Entry(self.window)
        self.address_label.pack()
        self.address_entry.pack()
        
        self.phone_label = tk.Label(self.window, text="Enter your phone number:")
        self.phone_entry = tk.Entry(self.window)
        self.phone_label.pack()
        self.phone_entry.pack()
        
        self.num_cars_label = tk.Label(self.window, text="Enter the number of cars you want to drive (Maximum of 5):")
        self.num_cars_entry = tk.Entry(self.window)
        self.num_cars_label.pack()
        self.num_cars_entry.pack()
        
        self.car_choices_label = tk.Label(self.window, text="Choose from the following cars:")
        self.car_choices_label.pack()
        
        self.car_choices = []
        self.car_choice_vars = []
        car_names = [
            "Lamborghini Gallardo",
            "Lamborghini Huracan",
            "Ferrari F40",
            "Porsche Boxster",
            "Audi AS",
            "BMW iB",
            "Lotus Elise"
        ]

        for i, car_name in enumerate(car_names):
            var = tk.IntVar()
            self.car_choice_vars.append(var)
            checkbox = tk.Checkbutton(self.window, text=car_name, variable=var)
            checkbox.pack()
            self.car_choices.append(checkbox)
        
        self.additional_laps_label = tk.Label(self.window, text="Do you want any additional laps (£15 per lap)? (Yes/No):")
        self.additional_laps_entry = tk.Entry(self.window)
        self.additional_laps_label.pack()
        self.additional_laps_entry.pack()
        
        self.calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate_cost)
        self.calculate_button.pack()
        
        self.bill_text = tk.Text(self.window)
        self.bill_text.pack()
        
    def calculate_cost(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone_number = self.phone_entry.get()
        num_cars = int(self.num_cars_entry.get())
        car_choices = [i+1 for i, var in enumerate(self.car_choice_vars) if var.get() == 1]
        additional_laps = int(self.additional_laps_entry.get())
        
        # Perform the cost calculation here
        
        # Update the bill text
        self.bill_text.delete(1.0, tk.END)
        self.bill_text.insert(tk.END, f"----- Bill -----\n")
        self.bill_text.insert(tk.END, f"Customer Details:\n")
        self.bill_text.insert(tk.END, f"Name: {name}\n")
        self.bill_text.insert(tk.END, f"Address: {address}\n")
        self.bill_text.insert(tk.END, f"Phone Number: {phone_number}\n")
        self.bill_text.insert(tk.END, f"\nCar Choices:\n")
        for i, car_choice in enumerate(car_choices):
            self.bill_text.insert(tk.END, f"Car {i+1}: {car_choice}\n")
        self.bill_text.insert(tk.END, f"\nAdditional Laps: {additional_laps}\n")
        self.bill_text.insert(tk.END, f"\nBreakdown of Costs:\n")
        # Add the cost breakdown here
        
    def start(self):
        self.window.mainloop()

def main():
    car_rental_gui = CarRentalGUI()
    car_rental_gui.start()

if __name__ == "__main__":
    main()