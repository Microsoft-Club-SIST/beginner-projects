from tkinter import *

# Define the available units
massUnitOptions = ["kg", "lb"]
heightUnitOptions = ["m", "cm", "inches"]

root = Tk()
root.title("BMI Calculator")
root.geometry("500x300")

# submit() function performs the necessary calculations
def submit():
	mass = float(massInput.get())
	height = float(heightInput.get())
	mass_unit = massUnits.get()
	height_unit = heightUnits.get()

	if mass_unit == "lb":
		mass /= 2.205
	if height_unit == "cm":
		height /= 100
	if height_unit == "inches":
		height /= 39.37

	bmi = mass/(height**2)
	bmiLabel.config(text = round(bmi, 3))

massUnits = StringVar()
massUnits.set(massUnitOptions[0])

heightUnits = StringVar()
heightUnits.set(heightUnitOptions[0])

# arrange all the widgets on the screen
massLabel = Label(root, text = "Enter your weight :", font = "bold")
massLabel.grid(row = 0, column = 0, padx = 35, pady = 20)

massInput = Entry(root, justify = "center", font = "bold")
massInput.grid(row = 0, column = 1)

massOptions = OptionMenu(root, massUnits, *massUnitOptions)
massOptions.grid(row = 0, column = 2, padx = 5)

heightLabel = Label(root, text = "Enter your height :", font = "bold")
heightLabel.grid(row = 1, column = 0)

heightInput = Entry(root, justify = "center", font = "bold")
heightInput.grid(row = 1, column = 1)

heightOptions = OptionMenu(root, heightUnits, *heightUnitOptions)
heightOptions.grid(row = 1, column = 2, padx = 5)

submitBtn = Button(root, text = "OK", command = submit, padx = 10)
submitBtn.grid(row = 2, column = 0, columnspan = 2, pady = 25)

info = Label(root, text = "Your Body Mass Index (BMI) is", font = "bold")
info.grid(row = 3, column = 0, columnspan = 2)

bmiLabel = Label(root, text = "", font = "bold")
bmiLabel.grid(row = 4, column = 0, columnspan = 2)

root.mainloop()
