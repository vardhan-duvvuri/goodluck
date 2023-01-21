'''
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''




Availableamount = 0

while True:

	inp = input('enter the transaction log:')

	if not inp:
		break
	else:
		t,a = inp.split(' ')
		if t == 'D' or t == 'W':
			if t == 'D':
				Availableamount += int(a)
			else:
				Availableamount -= int(a)
		else:
			print('transaction type is not valid, please enter the valid trasaction')



print(Availableamount)

