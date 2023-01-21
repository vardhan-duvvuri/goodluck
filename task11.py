'''
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

biary_nums = input("Enter binary numbers : ").split(",")
#### Method1
# out = []
# for num in biary_nums:
    # int_num = 0
    # for index,number in enumerate(num[::-1]):
    #     if int(number) == 1:
    #         int_num += 2**int(index)
    # if int_num > 0 and int(int_num)%5 == 0:
    #     out.append(num)
#### Method2
out = [num for num in biary_nums if int(num,2)%5 == 0]

print(",".join(out))