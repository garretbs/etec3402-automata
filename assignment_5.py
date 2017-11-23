#Garret Stevens

def a():
	state = 0
	final = [4, 5]
	for c in stra:
		if state == 0:
			if c == '/':
				state = 1
			else:
				return False
		elif state == 1:
			if c == '/':
				state = 5
			elif c == '*':
				state = 2
		elif state == 2:
			if c == '*':
				state = 3
		elif state == 3:
			if c == '/':
				state = 4
			elif c == '*':
				pass
			else:
				state = 2
		elif state == 4:
			return False
	if state in final:
		return True
	return False

def b():
	state = 0
	final = [1]
	alphabet1 = "_AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
	alphabet2 = "0123456789"
	for c in stra:
		if state == 0:
			if c in alphabet1: #is a letter
				state = 1
			else:
				return False
		elif state == 1:
			if c not in alphabet1 and c not in alphabet2: #not a letter or digit
				return False
	if state in final:
		return True
	return False

def c():
	state = 0
	final = [3]
	alphabet = "0123456789AaBbCcDdEeFf"
	for c in stra:
		if state == 0:
			if c == '0':
				state = 1
			else:
				return False
		elif state == 1:
			if c == 'x' or c == 'X':
				state = 2
			else:
				return False
		elif state == 2:
			if c in alphabet:
				state = 3
			else:
				return False
		elif state == 3:
			if c not in alphabet:
				return False
	if state in final:
		return True
	return False

def d():
	state = 0
	final = [2]
	for c in stra:
		if state == 0:
			if c == '"':
				state = 1
			else:
				return False
		elif state == 1:
			if c == '"':
				state = 2
			elif c == '\\':
				state = 3
		elif state == 2:
			return False
		elif state == 3:
			state = 1
	if state in final:
		return True
	return False

def e():
	state = 0
	final = [8, 10]
	numbers = "0123456789"
	for c in stra:
		if state == 0:
			if c == '1':
				state = 1
			elif c == '0':
				state = 11
			else:
				return False
		elif state == 1:
			if c in "012":
				state = 2
			else:
				return False
		elif state == 2:
			if c  == '/':
				state = 3
			else:
				return False
		elif state == 3:
			if c in "12":
				state = 4
			elif c == '0':
				state = 12
			elif c == '3':
				state = 13
			else:
				return False
		elif state == 4:
			if c in numbers:
				state = 5
			else:
				return False
		elif state == 5:
			if c == '/':
				state = 6
			else:
				return False
		elif state == 6:
			if c in numbers:
				state = 7
			else:
				return False
		elif state == 7:
			if c in numbers:
				state = 8
			else:
				return False
		elif state == 8:
			if c in numbers:
				state = 9
			else:
				return False
		elif state == 9:
			if c in numbers:
				state = 10
			else:
				return False
		elif state == 10:
			return False
		elif state == 11:
			if c in "123456789":
				state = 2
			else:
				return False
		elif state == 12:
			if c in "123456789":
				state = 5
			else:
				return False
		elif state == 13:
			if c in "01":
				state = 5
			else:
				return False
	if state in final:
		return True
	return False


stra = input("Input string: ")
if a():
	print("Valid C-style comment.")
if b():
	print("Valid C identifier.")
if c():
	print("Valid C hexadecimal.")
if d():
	print("Valid C string constant.")
if e():
	print("Valid date.")