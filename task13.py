'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

sentence = input("Enter Sentence : ")
digits = 0
chars = 0
for char in sentence:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        chars += 1

print("LETTERS : {}".format(chars))
print("DIGITS : {}".format(digits))


## TASK without in built function
# a-z to get digits
# 0-9 to get numbers
# [\w\d]+