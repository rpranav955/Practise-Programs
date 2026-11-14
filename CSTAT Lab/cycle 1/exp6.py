s = input("Enter your String: ").lower()

num_of_vowels = 0
num_of_consonants = 0
num_of_words = 1
num_of_qnmarks = 0

for ch in s:
	if ch in "aeiou":
		num_of_vowels += 1
	elif ch.isalpha():
		num_of_consonants += 1
	elif ch == ' ':
		num_of_words += 1
	elif ch == '?':
		num_of_qnmarks += 1
		
print("Number of vowels:\t\t", num_of_vowels)
print("Number of consonants:\t\t", num_of_consonants)
print("Number of words:\t\t", num_of_words)
print("Number of question marks:\t", num_of_qnmarks)
