def fibo(num):
	if(num == 1):
		return 0
	elif(num == 2):
		return 1
	else:
		return fibo(num - 1) + fibo(num - 2)
		
num = int(input("Enter the number: "))

print(num, "th Fibonacci Number is", fibo(num))
