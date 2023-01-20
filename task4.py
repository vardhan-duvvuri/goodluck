'''
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
'''

input_numbers = input("Enter the numbers:")

input_list = input_numbers.split(',') # Join to merge the things and split to separate the things

output_list = [int(i) for i in input_numbers.split(',')]

tuple_list = tuple(input_list)

print(input_list)
print(output_list)
print(tuple_list)