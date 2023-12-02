import tkinter as tk
import random
import time

def generate_random_word():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return random.choice(words)

def start_typing_test():
    num_words = 5  # Number of words to be typed
    typing_speed = 0  # Initialize typing speed counter
    start_time = time.time()  # Start the timer

    def check_typed_word(event):
        nonlocal typing_speed
        typed_word = entry.get()
        if typed_word == word_label["text"]:
            typing_speed += 1
        entry.delete(0, tk.END)
        if typing_speed < num_words:
            word_label["text"] = generate_random_word()
        else:
            end_time = time.time()
            total_time = end_time - start_time
            typing_speed = num_words / total_time
            speed_label["text"] = f"Typing Speed: {typing_speed:.2f} words per second"

    word_label["text"] = generate_random_word()
    entry.bind("<Return>", check_typed_word)
    entry.focus_set()

root = tk.Tk()
root.title("Speed Typing Test")
root.geometry("300x150")

word_label = tk.Label(root, text="")
word_label.pack()

entry = tk.Entry(root)
entry.pack()

speed_label = tk.Label(root, text="")
speed_label.pack()

start_button = tk.Button(root, text="Start", command=start_typing_test)
start_button.pack()

root.mainloop()
