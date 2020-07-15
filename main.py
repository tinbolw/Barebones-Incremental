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

valueLabel = tk.Entry(root)

valueLabel.pack()

valueButton = tk.Button(root, width=15, height=5, text = "Button", command = addToValue)
valueButton.pack()

root.mainloop()


