
def match(c):
	global ci
	global err_count
	print("Matching", c, "...")
	if c != stra[ci]:
		err_count += 1
	if ci < len(stra)-1:
		ci += 1

def S():
	if stra[ci] == 'a':
		match('a')
		B()
		B()

def B():
	if stra[ci] != 'c':
		error()
	match('c')
	if stra[ci] == 'b':
		Bp()

def Bp():
	match('b')
	S()
	if stra[ci] != 'b':
		error()
	match('b')
	if stra[ci] == 'b':
		Bp()

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