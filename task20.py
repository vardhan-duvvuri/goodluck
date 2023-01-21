'''
Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints:
Consider use yield
'''
class DivideBySeven():
    def getDivisibleNumbers(self,n):
        # for i in range(n+1):
        #     if i%7 == 0:
        #         yield i
        for i in range(0,n+1,7):
            yield i
n = int(input("Enter n: "))
d = DivideBySeven()
print(d.getDivisibleNumbers(n))
for num in d.getDivisibleNumbers(n):
    print(num)