num = int(input("Enter your number: "))

print()
print("Multiplication Table of ", num)
count = 1

while count <= 10:
	print(num, " x ", count, " = ", num*count)
	count += 1
