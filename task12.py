'''
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that
each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

out = []
# for num in range(1000,3001):
#     temp = True
#     for digit in str(num):
#         if not int(digit) % 2 == 0:
#             temp = False
#             break
#     if temp:
#         out.append(num)

def div(num):
    temp = True
    for digit in str(num):
        if not int(digit) % 2 == 0:
            temp = False
            break
    if temp:
        return True

out = filter(div, list(range(1000,3001)))

print(",".join([str(x) for x in out]))


## TASK : Try to solve this using map or filter function