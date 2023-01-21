'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

# inp = int(input('enter the digit between 0-9:'))


# out = inp+(inp*11)+(inp*111)+(inp*1111)

# print(out)



# ip = input('Enter Number:')
# num1 = ip*1
# num2 = ip*2
# num3 = ip*3
# num4 = ip*4
# sum = int(num1)+int(num2)+int(num3)+int(num4)
# print(sum)

ip = input('Enter Number:')
r = int(input('enter the range:'))

out = 0
for i in range(1,r+1):
	out += int(ip*i)

print(out)