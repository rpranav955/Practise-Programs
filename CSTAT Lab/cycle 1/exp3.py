s = input("Enter brackets: ")
stack = []
pairs = {')' : '(', '}' : '{', ']' : '['}

valid = True

for ch in s:
	if ch in "({[":
		stack.append(ch)
	elif ch in ")}]":
		if not stack or stack.pop() != pairs[ch]:
			valid = False
			break
			
if valid and not stack:
	print("Valid")
else:
	print("Invalid")
