
def match(c):
	global ci
	global err_count
	print("Matching", c, "...")
	if c != stra[ci]:
		err_count += 1
	if ci < len(stra)-1:
		ci += 1

def S():
	if stra[ci] == '(':
		match('(')
		S()
		if stra[ci] != ')':
			error()
			return
		match(')')
		S()
	elif stra[ci] in "01":
		match(stra[ci])
	else:
		error()
		
def A():
	if stra[ci] == '0':
		match('0')
	elif stra[ci] == '1':
		match('1')

def error():
	global err_count
	print("Unexpected character", stra[ci])
	err_count += 1



#S -> (S)S | 0 | 1


stra = input("Enter string: ")
ci = err_count = 0
stra = stra.strip() + chr(0)
S()
match(chr(0))
if err_count == 0:
	print("Derivation found!")
else:
	print("No derivation found.")