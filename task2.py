'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def factorial(x):
	out = 1
	for i in range(2,x+1):
		out *= i
	return out

x=int(input("Enter a num:"))
print(factorial(x))

def factorial_new(n):
    if n==1:
        return 1
    else:
        return n*factorial_new(n-1)

x=int(input("Enter a num:"))
print(factorial_new(x))


x=int(input("Enter a num:"))
out = 1
while True:
	if x == 1:
		break
	out *= x
	x -= 1
print(out)

import functools
x=int(input("Enter a num:"))

def fact(a,b):
	return a*b

print(functools.reduce(fact, list(range(1,x+1))))


inp = [[1,2,3],[4,5,6,7],[8,9]]
# out = [1,2,3,4,5,6,7,8,9]

# out = [x for i in inp for x in i]
# print(out)


out = []
def flat(i):
	if not(bool(i)):
		return i
	if isinstance(i[0], list):
		return flat(*i[:1]) + flat(i[1:])
	return i[:1] + flat(i[1:])
out = flat(inp)
print(out)