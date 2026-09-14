filename = "sample.txt"

with open(filename, 'r') as file:
    text = file.read()

word_count = len(text.split())

sentence_count = text.count('.') + text.count('!') + text.count('?')

upper_count = 0
lower_count = 0
special_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif not char.isspace() and not char.isalnum():
        special_count += 1

print("Words:", word_count)
print("Sentences:", sentence_count)
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
print("Special symbols:", special_count)
