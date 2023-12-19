import tkinter as tk

# Function to clear text entry boxes
def clearAll():
    word1_field.delete(0, tk.END)
    word2_field.delete(0, tk.END)

# Function to perform correction
def correction():
    input_word = word1_field.get()
    corrected_word = "corrected_word"  # Replace with your correction logic
    word2_field.insert(10, corrected_word)
    clearAll()

# Create the main window
root = tk.Tk()
root.configure(bg="light green")
root.geometry("400x150")
root.title("Spell Corrector")

# Create labels
welcome_label = tk.Label(root, text="Welcome to Spell Corrector Application")
input_label = tk.Label(root, text="Input Word")
corrected_label = tk.Label(root, text="Corrected Word")

# Position labels using grid method
welcome_label.grid(row=0, column=0, columnspan=2)
input_label.grid(row=1, column=0)
corrected_label.grid(row=2, column=0)

# Create text entry boxes
word1_field = tk.Entry(root)
word2_field = tk.Entry(root)

# Position text entry boxes using grid method
word1_field.grid(row=1, column=1)
word2_field.grid(row=2, column=1)

# Clear text entry boxes and perform correction
clearAll()
correction()

# Start the main event loop
root.mainloop()
