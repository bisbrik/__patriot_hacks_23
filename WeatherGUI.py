# Import Module
from tkinter import *
from PIL import ImageTk,Image,ImageDraw, ImageFilter
import os
from weather_API import weather_API
from weather_clothing import weather_clothing

# create root window
root = Tk()

# Set the current working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)
image = Image.open("sprite.png")
resize_image = image.resize((60, 130))

#img = ImageTk.PhotoImage(resize_image)
#label = Label(image=img)
#label.image = img
#label.grid(row=0)

photo = ImageTk.PhotoImage(image)
label = Label(root, image = photo)
label.image = photo
label.grid(row=0)

def showClothes(array):

	for string in array: 

		if string == "shortSleeves":
			imageShortSleeve = Image.open("shortSleeve.png")
			image.paste(imageShortSleeve, (0,0), mask = imageShortSleeve)

		if string == "longSleeves":
			imageLongSleeve = Image.open("longSleeve.png")
			image.paste(imageLongSleeve, (0,0), mask = imageLongSleeve)

		if string == "shortPants":
			imageShortPants = Image.open("shortPants.png")
			image.paste(imageShortPants, (0,0), mask = imageShortPants)

		if string == "longPants":
			imageLongPants = Image.open("longPants.png")
			image.paste(imageLongPants, (0,0), mask = imageLongPants)

		if string == "sunglasses":
			imageSunglasses = Image.open("sunglasses.png")
			image.paste(imageSunglasses, (0,0), mask = imageSunglasses)

		if string == "hat":
			imageHat = Image.open("hat.png")
			image.paste(imageHat, (0,0), mask = imageHat)

		if string == "umbrella":
			imageUmbrella = Image.open("umbrella.png")
			image.paste(imageUmbrella, (0,0), mask = imageUmbrella)
			imageUmbrellaPaste = Image.open("umbrellaPaste.png")
			imageUmbrella.paste(imageUmbrellaPaste, (0,0), mask = imageUmbrellaPaste)

string_input = {"shortPants", "longSleeves"}
showClothes(string_input)


# Update the Tkinter display
#photo = ImageTk.PhotoImage(image)
#label.configure(image=photo)
#label.image = photo

# Update the Tkinter display
photo = ImageTk.PhotoImage(image)
label.configure(image=photo)
label.image = photo

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

# function to display user text when button is clicked
def clicked():
	res = "Weather for: " + txt.get()
	lbl.configure(text = res)
	print("hello world")
	res  = "getting the weather..."
	weatherApi = weather_API()
	weatherApi.get_averages(txt.get())
	print(weatherApi.get_data_list())
	

# button widget with red color text inside
btn = Button(root, text = "Tell me the weather!" ,
			fg = "red", command=clicked)

# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
