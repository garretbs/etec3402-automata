
def match(c):
	global ci
	global err_count
	print("Matching", c, "...")
	if c != stra[ci]:
		err_count += 1
	if ci < len(stra)-1:
		ci += 1

def S():
	if stra[ci] != 'a':
		error()
	match('a')
	if stra[ci] != 'a':
		error()
	match('a')
	if stra[ci] == 'b':
		match('b')
		B()
		if stra[ci] != 'b':
			error()
		match('b')

def B():
	if stra[ci] == 'b':
		match('b')
		B()
		if stra[ci] != 'b':
			error()
		match('b')
	if stra[ci] != 'a':
		error()
	match('a')

def error():
	global err_count
	print("Unexpected character", stra[ci])
	err_count += 1



stra = input("Enter string: ")
ci = err_count = 0
stra = stra.strip() + chr(0)
S()
match(chr(0))
if err_count == 0:
	print("Derivation found!")
else:
	print("No derivation found.")