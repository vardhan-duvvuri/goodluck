'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
'''

class Firstclass:

	def __init__(self):
		self.input_string = ''

	def setstringvalue(self):
		self.input_string = input("enter the string:")

	def getstringvalue(self):
		return self.input_string

	def printstringvalue(self):
		outputstring = self.getstringvalue()
		print("the input string in upper case:", outputstring.upper())

obj = Firstclass()
obj.setstringvalue()
obj.printstringvalue()