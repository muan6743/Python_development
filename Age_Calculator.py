import tkinter as tk
from datetime import date

def calculate_age():
    birth_year = int(entry_year.get())
    current_year = date.today().year
    age = current_year - birth_year
    label_result.config(text=f"Your age is: {age}")

# Create the main window
window = tk.Tk()
window.title("Age Calculator")

# Create widgets
label_year = tk.Label(window, text="Enter your birth year:")
label_year.pack()

entry_year = tk.Entry(window)
entry_year.pack()

button_calculate = tk.Button(window, text="Calculate", command=calculate_age)
button_calculate.pack()

label_result = tk.Label(window)
label_result.pack()

# Start the event loop
window.mainloop()
