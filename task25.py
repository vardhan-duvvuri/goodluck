'''
Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

# class Classtest:
# 	c1 = 'xyz'

# 	def __init__(self,c1):
# 		self.c1 = c1

# obj = Classtest('abc')
# print(obj.c1)

##### set the value later ####

class Classtest:
	c1 = 'xyz'

	def __init__(self):
		self.c1 = None

obj = Classtest()
obj.c1 = 'abc'
print(obj.c1)

print(Classtest.c1)