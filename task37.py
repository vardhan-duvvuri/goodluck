'''
Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.

Hints:

Use ** operator to get power of a number.
Use range() for loops.
Use list.append() to add values into a list.
Use [n1:n2] to slice a list
'''

l1 = []

for i in range(1,21):
	l1.append(i**2)
print(l1)

print(l1[:5])

print(l1[::2])

print(l1[-4:-6:-1])

print(l1[-2::-1])
