db = {}

def signup(name, pin):
	if db.get(name) != None:
		db[name][1] = pin
	db[name] = [pin, 0]

def signin(name, pin):
	if db.get(name) == None:
		return -1 # for name not exist
	elif db[name][0] != pin:
		return -2 # for pin incorrect
	else:
		return 0 # for success

def check(name):
	if db.get(name) == None:
		return -1 # for name not exist
	return db[name][1]


def deposit(name, amount):
	if db.get(name) == None:
		return -1 # for name not exist
	db[name][1] += amount
	return 0

def extract(name, amount):
	if db.get(name) == None:
		return -1 # for name not exit
	if amount > db[name][1]:
		return -3 # for not enough money
	db[name][1] -= amount
	return 0

def session():
	name = input('Name: ')
	pin = input('PIN: ')
	ret = signin(name, pin)
	if ret == -1:
		print('Name not exist')
		return -1
	elif ret == -2:
		print('PIN incorrect')
		return -2
	else:
		while True:
			op = input('[C]heck balance, [E]xtract, [D]eposit, or [L]eave: ')
			if op.lower() == 'c':
				print(check(name))
			elif op.lower() == 'e':
				amount = int(input('Enter amount: '))
				if extract(name, amount) == -3:
					print('Not enough money')
			elif op.lower() == 'd':
				amount = int(input('Enter amount: '))
				deposit(name, amount)
			elif op.lower() == 'l':
				break
			else:
				print('Wrong command')

signup('test', '123')
while True:
	session()
