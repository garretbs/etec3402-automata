#Garret Stevens
alphabet = "abc"

def a(str):
	state = 0;
	final = [2]
	for c in str:
		if c not in alphabet:
			return False
		if state == 0:
			if c == 'a':
				state = 1
		elif state == 1:
			if c == 'a':
				pass
			elif c == 'b':
				state = 2
			elif c == 'c':
				state = 0
		elif state == 2:
			if c == 'a':
				state = 1
			else:
				state = 0
	if state in final:
		return True
	return False
	
def b(str):
	state = 0;
	final = [3]
	for c in str:
		if c not in alphabet:
			return False
		if state < 3:
			if c == 'a':
				state += 1
			else:
				state = 0
	if state in final:
		return True
	return False
	
def c(str):
	state = 0;
	final = [0, 1, 2, 3]
	for c in str:
		if c not in alphabet:
			return False
		if state == 0: #start state
			if c == 'a':
				state = 1
			elif c == 'b':
				state = 2
			elif c == 'c':
				state = 3
		if state == 1: #got an a
			if c == 'b' or c == 'c':
				state = 4
		if state == 2: #got a b
			if c == 'a' or c == 'c':
				state = 5
		if state == 3: #got a c
			if c == 'a' or c == 'b':
				state = 6
		if state == 4: #a and then something else
			if c == 'a':
				state = 1
		if state == 5: #b and then something else
			if c == 'b':
				state = 2
		if state == 6: #c and then something else
			if c == 'c':
				state = 3
	if state in final:
		return True
	return False
	
def d(str):
	state = 0;
	final = [3]
	for c in str:
		if c not in alphabet:
			return False
		if state < 4:
			state += 1
	if state in final:
		return True
	return False
	
def e(str):
	state = 0;
	final = [3]
	for c in str:
		if c not in alphabet:
			return False
		if state < 4:
			state += 1
	if state in final:
		return False
	return True
	
str = input("Input a string: ")
if a(str):
	print("Valid string ending in ab")
if b(str):
	print("Valid string containing 3 consecutive a's")
if c(str):
	print("Valid string starting and ending with the same symbol")
if d(str):
	print("Valid string with three symbols")
if e(str):
	print("Valid string that is not three symbols")