'''
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

.The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of 
movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''

import math

current_position = [0,0]
while True:
	inp = input('Enter the input tuples:')
	if inp:
		inp = inp.split(' ')
		dr,step = inp[0],float(inp[1])
		if dr == 'UP':
			current_position[0] += step
		elif dr == 'DOWN':
			current_position[0] -= step
		elif dr == 'LEFT':
			current_position[1] -= step
		elif dr == 'RIGHT':
			current_position[1] += step
	else:
		break

distance = int(math.sqrt(current_position[0]**2 + current_position[1]**2))
print(distance)






