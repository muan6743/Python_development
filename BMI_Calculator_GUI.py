# Import necessary libraries

import tkinter as tk
from tkinter import messagebox

# Define a function to calculate BMI

def calculate_bmi():
    weight = float(weight_entry.get()) # Get the weight from the weight_entry field and convert it to float
    height = float(height_entry.get()) # Get the height from the height_entry field and convert it to float
    bmi = weight / (height * height)  # Calculate the BMI

# Display the BMI in a message box

    messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")

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
