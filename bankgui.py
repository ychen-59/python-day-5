import tkinter as tk
from tkinter import messagebox as msgbox

FONT_MAIN = ('Arial', 11)
FONT_TITLE = ('Arial', 16, 'bold')

def signup():
	user = e_user.get()
	pwd = e_pwd.get()
	print(user, pwd)
	l_status.config(text='')

	if user == '' or pwd == '':
		l_status.config(text='Please fill in all fields.', fg='#d9534f')
		return

	if db.get(user) != None:
		db[user][1] = pwd
	db[user] = [user, 0]

	print(db)


def login():
	user = e_user.get()
	pwd = e_pwd.get()
	print(user, pwd)
	l_status.config(text='')

	if user == '' or pwd == '':
		l_status.config(text='Please fill in all fields.', fg='#d9534f')
		return

	if db.get(user) == None or db[user][0] != pwd:
		l_status.config(text='Invalid username or password.', fg='#d9534f')
		return
	show_dashboard(user)


def login_screen():
	for widget in root.winfo_children():
		widget.destroy()

	# Heading
	l_login = tk.Label(root, text='LOGIN', font=FONT_TITLE)
	l_login.pack(pady=20)

	# Username
	f_user = tk.Frame(root)
	f_user.pack()
	l_user = tk.Label(f_user, text='Username:', font=FONT_MAIN, width=10, anchor='w')
	l_user.pack(side=tk.LEFT)
	global e_user
	e_user = tk.Entry(f_user, width=15)
	e_user.pack(side=tk.LEFT)

	# Password
	f_pwd = tk.Frame(root)
	f_pwd.pack()
	l_pwd = tk.Label(f_pwd, text='Password:', font=FONT_MAIN, width=10, anchor='w')
	l_pwd.pack(side=tk.LEFT)
	global e_pwd
	e_pwd = tk.Entry(f_pwd, width=15, show='*')
	e_pwd.pack(side=tk.LEFT)

	tk.StringVar = ''

	# Login Button
	f_btn = tk.Frame(root)
	f_btn.pack(pady=15)
	btn_login = tk.Button(root, text='Log In', font=FONT_MAIN, width=15, command=login)
	btn_signup = tk.Button(
		root, text='Sign Up', font=FONT_MAIN, width=15, command=signup
	)
	btn_login.pack()
	btn_signup.pack()

	# Message
	global l_status
	l_status = tk.Label(root, text='', font=('Arial', 10))
	l_status.pack(pady=10)


def update_balance(val):
	l_balance.config(text=str(val))

def deposit():
	l_status.config(text='')
	user = tk.StringVar
	try:
		amount = int(e_deposit.get())
	except ValueError:
		l_status.config(text='Invalid amount.', fg='#d9534f')
		return

	db[user][1] += amount
	update_balance(db[user][1])


def withdraw():
	l_status.config(text='')
	user = tk.StringVar
	try:
		amount = int(e_withdraw.get())
	except ValueError:
		l_status.config(text='Invalid amount.', fg='#d9534f')
		return

	if amount > db[user][1]:
		l_status.config(text='Not enough money.', fg='#d9534f')
		return
	db[user][1] -= amount
	update_balance(db[user][1])

def show_dashboard(user):
	for widget in root.winfo_children():
		widget.destroy()

	# Padding
	l_pad = tk.Label(root, text='', font=FONT_TITLE)
	l_pad.pack(pady=20)

	tk.StringVar = user

	# Buttons
	f_balance = tk.Frame(root, width=15)
	f_balance.pack()
	l_balance_text = tk.Label(f_balance, text='Balance: ', font=FONT_MAIN, width=12, anchor='w')
	l_balance_text.pack(side=tk.LEFT)
	global l_balance
	l_balance = tk.Label(f_balance, text=str(db[user][1]), font=FONT_MAIN, width=7, anchor='e')
	l_balance.pack(side=tk.LEFT)

	f_deposit = tk.Frame(root)
	f_withdraw = tk.Frame(root)
	f_deposit.pack()
	f_withdraw.pack()

	btn_deposit = tk.Button(f_deposit, text='Deposit', font=FONT_MAIN, width=10, command=deposit)
	btn_deposit.pack(side=tk.LEFT)
	global e_deposit
	e_deposit = tk.Entry(f_deposit, width=5)
	e_deposit.pack()

	btn_withdraw = tk.Button(f_withdraw, text='Withdraw', font=FONT_MAIN, width=10, command=withdraw)
	btn_withdraw.pack(side=tk.LEFT)
	global e_withdraw
	e_withdraw = tk.Entry(f_withdraw, width=5)
	e_withdraw.pack()

	btn_exit = tk.Button(root, text='Exit', font=FONT_MAIN, width=16, command=login_screen)
	btn_exit.pack()

	# Message
	global l_status
	l_status = tk.Label(root, text='', font=('Arial', 10))
	l_status.pack(pady=10)


"""
Database
Key: Name
Value: List, [password, savings]
"""
db = {}

root = tk.Tk()
root.geometry('480x480')
root.resizable(False, False)

login_screen()

root.mainloop()
