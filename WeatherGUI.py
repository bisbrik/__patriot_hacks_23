# Import Module
from tkinter import *
from PIL import ImageTk,Image  
import os

# create root window
root = Tk()


# Set the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)

image = Image.open("sprite.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image = photo)
label.image = photo
label.grid(row=1)

#image2 = Image.open("shortSleeve.png")
#image.paste(image2, (0,0), mask = image2)

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
