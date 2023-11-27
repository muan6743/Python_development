import tkinter as tk
from tkinter import font
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

# Create the main window
window = tk.Tk()
window.title("Digital Clock")
window.geometry("300x100")
window.configure(bg="black")

# Create the clock label
clock_font = font.Font(family="Helvetica", size=48, weight="bold")
clock_label = tk.Label(window, font=clock_font, fg="white", bg="black", bd=4, relief="solid")
clock_label.pack(pady=20)

# Update the time every second
update_time()

# Start the main loop
window.mainloop()
