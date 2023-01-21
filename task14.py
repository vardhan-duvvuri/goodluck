'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''


# inp = input('Enter sentence:')

# upper = []
# lower = []
# uppercount = 0
# lowercount = 0
# for char in inp:
# 	if char.isupper():
# 		upper.append(char)
# 		uppercount += 1
# 	elif char.islower():
# 		lower.append(char)
# 		lowercount += 1

# print("count of upper case:", uppercount)
# print("count of lower case:", lowercount)


inp = input('Enter sentence:')

uppercount = 0
lowercount = 0
for char in inp:
	if char.isupper():
		uppercount += 1
	elif char.islower():
		lowercount += 1

print("count of upper case:", uppercount)
print("count of lower case:", lowercount)
