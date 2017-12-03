T_EOF = 0
T_LPAREN = 1
T_RPAREN = 2
T_OP1 = 3
T_OP2 = 4
T_NUM = 5

class Token(object):
	def __init__(self, token_type, token_lexeme, token_value):
		self.token_type = token_type
		self.token_lexeme = token_lexeme
		self.token_value = token_value
		
	def __repr__(self):
		return "token( type: "+str(self.token_type)+" lexeme: "+str(self.token_lexeme)+" value: "+str(self.token_value)+")\n"
		
def lexer(source_string):
	source_string += chr(0)
	token_list = []
	state = 0
	i = 0
	while True:
		c = source_string[i]
		i += 1
		if state == 0:
			if c == '(':
				token_list.append(Token(T_LPAREN, c, None))
			elif c == ')':
				token_list.append(Token(T_RPAREN, c, None))
			elif c == '+' or c == '-':
				token_list.append(Token(T_OP1, c, None))
			elif c in "*/%":
				token_list.append(Token(T_OP2, c, None))
			elif c in "0123456789":
				state = 1
				lexeme_temp = c
			elif c == chr(0):
				token_list.append(Token(T_EOF, c, None))
				break
			elif c == " ":
				pass
			else:
				print("fucking lexer error")
		elif state == 1:
			if c in "0123456789":
				lexeme_temp += c
			else:
				state = 0
				token_list.append(Token(T_NUM, lexeme_temp, int(lexeme_temp)))
				i -= 1
	return token_list
	
	
def get_current_token():
	return tokens[token_position]
	
def match(token_type):
	global token_position
	global err_count
	if token_type == get_current_token().token_type:
		token_position += 1
	else:
		print("Expected: ", str(token_type), " but got ", str(get_current_token().token_type))
		err_count += 1
	
def S():
	E()
	match(T_EOF)
	
def E():
	T()
	while get_current_token().token_type == T_OP1:
		match(T_OP1)
		T()

def T():
	F()
	while get_current_token().token_type == T_OP2:
		match(T_OP2)
		F()

def F():
	global err_count
	if get_current_token().token_type == T_LPAREN:
		match(T_LPAREN)
		E()
		match(T_RPAREN)
	elif get_current_token().token_type == T_NUM:
		match(T_NUM)
	else:
		print("Expected token: " + str(get_current_token().token_type))
		err_count += 1

err_count = 0
stra = input("Enter string: ")
stra = stra.strip() + chr(0)
token_position = 0
tokens = lexer(stra)
E()
if err_count == 0:
	print("Derivation found!")
else:
	print("No derivation found.")