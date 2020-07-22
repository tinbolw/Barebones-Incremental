import time
import tkinter as tk


value = 0
valueAdd = 1
passiveAdd = 0
root = tk.Tk()

root.title("Game")
root.geometry("400x400")

def addPassive():
	global value
	value = value + passiveAdd
	##TODO

def addToValue():
	global value
	global valueAdd
	value = value + valueAdd
	valueLabel.delete(0, tk.END)
	valueLabel.insert(0, value)

def buyUpgrade():
	global value
	global valueAdd
	if value >= 50:
		value = value - 50
		valueLabel.delete(0, tk.END)
		valueLabel.insert(0, value)
		valueAdd = valueAdd + 1
	else:
		valueLabel.delete(0, tk.END)
		valueLabel.insert(0, "Not Enough Money")

def buyAutobot():
	global value
	global passiveAdd
	if value >= 100:
		value = value - 100
		valueLabel.delete(0, tk.END)
		valueLabel.insert(0, value)
		passiveAdd = passiveAdd + 1

valueLabel = tk.Entry(root)
valueLabel.pack()

valueButton = tk.Button(root, width=15, height=5, text = "Button", command = addToValue)
valueButton.pack()

buyHelperButton = tk.Button(root, width=15, height=5, text="Buy Upgrade (50)", command=buyUpgrade)
buyHelperButton.pack()

buyAutobotButton = tk.Button(root, width=15, height=5, text="Buy Autobot (100)", command=buyAutobot)

addPassive()

root.mainloop()
