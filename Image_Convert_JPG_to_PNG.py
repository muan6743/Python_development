
from tkinter import Tk, Button, filedialog
import os
from PIL import Image

def convert_image():
    # Open the file dialog to select the JPG image
    jpg_path = filedialog.askopenfilename(filetypes=[("JPG Files", "*.jpg")])
    

    if jpg_path:
        # Load the JPG image
        image_path = os.path.join("G:\Projects\Python_development\Img", "men.jpg")
        image = Image.open(image_path)
        
        # Convert the image to PNG format
        png_path = jpg_path.replace(".jpg", ".png")
        image.save(png_path, "PNG")
        
        # Display a success message
        print("Image converted successfully!")
    else:
        # Display an error message if no file was selected
        print("No file selected.")

# Create the GUI window
window = Tk()

# Create a button to trigger the image conversion
convert_button = Button(window, text="Convert Image", command=convert_image)
convert_button.pack()

# Start the GUI event loop
window.mainloop()
