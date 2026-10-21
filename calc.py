import tkinter as tk

# Create the main window
root = tk.Tk()
root.title('Calculator')
root.geometry('320x450')
root.resizable(False, False)
root.configure(bg='#222831')

# Display
expression = ''

display = tk.Entry(
	root, font=('Arial', 24), justify='right', bg='#393E46', fg='white', bd=0
)
display.pack(fill='x', padx=10, pady=15, ipady=15)


def click(value):
	if value == 'C':
		display.delete(0, tk.END)

	elif value == '=':
		try:
			result = eval(display.get())
			display.delete(0, tk.END)
			display.insert(tk.END, str(result))
		except Exception:
			display.delete(0, tk.END)
			display.insert(tk.END, 'Error')

	else:
		display.insert(tk.END, value)


# Button layout
buttons = [
	['7', '8', '9', '/'],
	['4', '5', '6', '*'],
	['1', '2', '3', '-'],
	['C', '0', '.', '+'],
	['='],
]

# Create buttons
for row in buttons:
	frame = tk.Frame(root, bg='#222831')
	frame.pack(expand=True, fill='both', padx=5)

	for char in row:
		btn = tk.Button(
			frame,
			text=char,
			font=('Arial', 18, 'bold'),
			bg='#00ADB5' if char in '+-*/=' else '#393E46',
			fg='white',
			activebackground='#00ADB5',
			bd=0,
			command=lambda c=char: click(c),
		)
		btn.pack(side='left', expand=True, fill='both', padx=3, pady=3)

# Run the application
root.mainloop()
