# Import Module
from tkinter import *
from PIL import ImageTk,Image  
import os

# create root window
root = Tk()


# Set the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

# Specify the path to the image file
image_path = "sprite.png"

# Check if the image file exists in the current directory

#if os.path.exists(image_path):
#    print(f"The image file '{image_path}' exists in the current directory.")
#    img = ImageTk.PhotoImage(Image.open(image_path))
#    canvas = Canvas(root, width=300, height=300)
#    canvas.pack()
#   canvas.create_image(20, 20, anchor=NW, image=img)
#else:
#    print(f"The image file '{image_path}' does not exist in the current directory.")


# Define the geometry of the window

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("sprite.png"))
# Create a Label Widget to display the text or Image
label = Label(root, image = img)
label.pack()


# root window title and dimension
root.title("Welcome to the Weather App!")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "What is your zipcode?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when 
# button is clicked
def clicked():

	res = "Weather for: " + txt.get()
	lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Tell me the weather!" ,
			fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
