import random

NOUN = ['man ', 'woman ', 'student ', 'teacher ', 'programmer ', 'geek ', 'nerd ', 'genius ', 'princess ', 'prince ', 'ninja ', 'wizard ', 'toad ']

DET = ['a ', 'the ', 'some ', 'that ', 'this ']
HPV = ['is ', 'was ']
CONJ = ['and ', 'or ', 'but ']
ADV = ['sometimes ', 'often ', 'never ', 'always ']
ADJ = ['happy ', 'sad ', 'good ', 'bad ', 'clever ', 'lazy ', 'brilliant ', 'stupid ', 'lame ', 'useless ', 'crazy ', 'silly ']

PNOUN = ['Ted ', 'Paul ', 'Jason ', 'Jim ', 'Mario ', 'Harry Potter ', 'Gandalf ', 'Ada ']
ENDP = ['.', '!', '?']

sent = {}
sent[0] = [1, 2]
sent[1] = [2]
sent[2] = [3]
sent[3] = [4]
sent[4] = [5, 6, 7]
sent[5] = [5, 6]
sent[6] = [8]
sent[7] = [7, 8]
sent[8] = [0, 3, 9]





#print("Generating random sentence...")
state = 0
next = -1
sentence = ""
while state != 9:
	next = random.choice(sent[state])
	if state == 0:
		if next == 1:
			sentence += random.choice(DET)
		elif next == 2:
			sentence += random.choice(PNOUN)
	if state == 1:
		if next == 2:
			sentence += random.choice(NOUN)
	if state == 2:
		if next == 3:
			sentence += random.choice(HPV)
	if state == 3:
		if next == 4:
			sentence += random.choice(ADV + [''])
	if state == 4:
		if next == 5:
			sentence += random.choice(DET)
		elif next == 6:
			sentence += random.choice(DET)
		elif next == 7:
			pass
	if state == 5:
		if next == 5:
			sentence += random.choice(ADJ)
		elif next == 6:
			sentence += random.choice(ADJ)
	if state == 6:
		if next == 8:
			sentence += random.choice(NOUN)
	if state == 7:
		if next == 7:
			sentence += random.choice(ADJ)
		elif next == 8:
			sentence += random.choice(ADJ)
	if state == 8:
		if next == 0:
			sentence += random.choice(CONJ)
		elif next == 3:
			sentence += random.choice(CONJ)
		elif next == 9:
			sentence = sentence[:-1]
			sentence += random.choice(ENDP)
	state = next
print(sentence)