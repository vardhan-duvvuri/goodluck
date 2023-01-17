"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line."""

# output = []
# for num in range(2000, 3201):
# 	if num%7 == 0 and num%5 !=0:
# 		output.append(num)
# print(",".join([str(x) for x in output]))

# output = ",".join([str(x) for x in range(2000, 3201) if x%7 ==0 and x%5 != 0])
# print(output)

# def find(num):
# 	if num%7 == 0 and num%5 !=0:
# 		return True

# inp = list(range(2000,3201))
# out = list(filter(find, inp))
# print(",".join([str(x) for x in out]))


##MAP

inp = [1,2,3,4,5]
out = [1,4,9,16,25]

def sq(num):
	return num**2
print(list(map(sq, inp)))


##FILTER

inp = [1,2,3,4,5]
out = [1,3,5]

def odd(num):
	if num%2 != 0:
		return True
print(list(filter(odd,inp)))

##REDUCE
import functools

inp = [1,2,3,4,5]
out = 15

def summ(a,b):
	return a*b

print(functools.reduce(summ, inp))

out = 1
for i in inp:
	out *= i
print(out)