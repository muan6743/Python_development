# Import necessary libraries

import tkinter as tk
from tkinter import messagebox

# Define a function to calculate BMI

def calculate_bmi():
    weight = float(weight_entry.get()) # Get the weight from the weight_entry field and convert it to float
    height = float(height_entry.get()) # Get the height from the height_entry field and convert it to float
    height = height / 100 # Convert the height from centimeters to meters
    bmi = weight / (height * height)  # Calculate the BMI
    
    if bmi > 0:
        if bmi <= 16:
            print("you are severely underweight")
        elif bmi <= 18.5:
            print("you are underweight")
        elif bmi <= 25:
            print("you are Healthy")
        elif bmi <= 30:
            print("you are overweight")
        else:
            print("you are severely overweight")

    # Display the BMI in a message box
    messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.3f}")

# Create the GUI window
window = tk.Tk()
window.title("BMI Calculator")

# Create a label to instruct the user to enter their weight 
instruction_label = tk.Label(window, text="Enter your weight in kilograms:")
instruction_label.pack()

# Create an entry field for the user to enter their weight
weight_entry = tk.Entry(window)
weight_entry.pack()

# Create a label to instruct the user to enter their height
height_label = tk.Label(window, text="Enter your height in meters:")
height_label.pack()

height_entry = tk.Entry(window)
height_entry.pack()

# Create a button to trigger the BMI calculation
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Start the GUI
window.mainloop()
