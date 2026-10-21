import tkinter as tk


def handle_login():
	username = entry_user.get()
	password = entry_pass.get()

	# Clear previous status style
	label_status.config(text='')

	# Inline Validation
	if not username or not password:
		label_status.config(
			text='⚠️ Please fill in all fields.', fg='#d9534f'
		)  # Red warning
		return

	if username == 'admin' and password == 'password123':
		label_status.config(
			text='✅ Login successful! Redirecting...', fg='#5cb85c'
		)  # Green success
	else:
		label_status.config(
			text='❌ Invalid username or password.', fg='#d9534f'
		)  # Red error


# Initialize main window
root = tk.Tk()
root.title('Login Window')
root.geometry('400x330')
root.resizable(False, False)

# Styling variables
FONT_MAIN = ('Arial', 11)
FONT_TITLE = ('Arial', 16, 'bold')

# Title Label
label_title = tk.Label(root, text='Welcome Back', font=FONT_TITLE)
label_title.pack(pady=20)

# Username Field
frame_user = tk.Frame(root)
frame_user.pack(pady=5)
label_user = tk.Label(
	frame_user, text='Username:', font=FONT_MAIN, width=10, anchor='w'
)
label_user.pack(side=tk.LEFT)
entry_user = tk.Entry(frame_user, font=FONT_MAIN, width=15)
entry_user.pack(side=tk.LEFT)

# Password Field
frame_pass = tk.Frame(root)
frame_pass.pack(pady=10)
label_pass = tk.Label(
	frame_pass, text='Password:', font=FONT_MAIN, width=10, anchor='w'
)
label_pass.pack(side=tk.LEFT)
entry_pass = tk.Entry(frame_pass, font=FONT_MAIN, width=15, show='*')
entry_pass.pack(side=tk.LEFT)

# Login Button
btn_login = tk.Button(
	root,
	text='Log In',
	font=FONT_MAIN,
	bg='#4CAF50',
	fg='white',
	width=15,
	command=handle_login,
)
btn_login.pack(pady=10)

# Inline Status / Error Message Label (acts like a web notification banner)
label_status = tk.Label(root, text='', font=('Arial', 10), wraplength=280)
label_status.pack(pady=10)

# Run the application
root.mainloop()
