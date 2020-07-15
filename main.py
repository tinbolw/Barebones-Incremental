import time
import tkinter as tk


value = 0
valueAdd = 1
root = tk.Tk()

root.title("Game")
root.geometry("400x400")

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

valueLabel = tk.Entry(root)
valueLabel.pack()

valueButton = tk.Button(root, width=15, height=5, text = "Button", command = addToValue)
valueButton.pack()

buyHelperButton = tk.Button(root, width=10, height=3, text="Buy Upgrade \(50\), command=buyUpgrade)
buyHelperButton.pack()

root.mainloop()


