
def match(c):
	global ci
	global err_count
	print("Matching", c, "...")
	if c != stra[ci]:
		err_count += 1
	if ci < len(stra)-1:
		ci += 1

def E():
	if stra[ci] == '\0':
		return
	T()
	while stra[ci] in "-+":
		match(stra[ci])
		T()

def T():
	F()
	while stra[ci] in "/*%":
		match(stra[ci])
		F()

def F():
	if stra[ci] == '-':
		match('-')
	if stra[ci] not in "0123456789":
		match('(')
		E()
		match(')')
	while stra[ci] in "0123456789":
		match(stra[ci])

def error():
	global err_count
	print("Unexpected character", stra[ci])
	err_count += 1



stra = input("Enter string: ")
ci = err_count = 0
stra = stra.strip() + chr(0)
E()
match(chr(0))
if err_count == 0:
	print("Derivation found!")
else:
	print("No derivation found.")