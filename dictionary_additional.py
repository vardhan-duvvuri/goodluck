d = {}
for i in range(1,21):
    d[i] = i**2
print(d)
# print(d[10])

# for i in d.keys():
#     print(i, d[i])
#
# for i in d.values():
#     print(i)

# for key,value in d.items():
#     if value == 401:
#         print(key)

# print(d.get(22))
# print(d[22])


# print(dict.__doc__)


# def myFunction(**kwargs):
#     sum = 0
#     for kw in kwargs:
#         sum += kwargs[kw]
#     print(sum)
#
# if __name__ == "__main__":
#     # d = {'a':24,'b':87,'c':3,'d':46}
#     myFunction(a=24,b=87,c=3,d=46)

# def myFunction(*args):
#     sum = 0
#     for ele in args:
#         sum +=ele
#     print(sum)
#
# if __name__ == "__main__":
#     myFunction(24,87, 3, 46)

# d2 = d.copy()
# d.pop(15)
# d.popitem()
# d.update({11:'aaaa'})
# print(d)
#
# # d2 = d.copy()
# print(d2)

from copy import deepcopy
# l1 = [1,2,3,4]
# l2 = l1
# l1.append(5)
# d.setdefault()

# d.setdefault(21,441)
# if d.get(21):
#     print(d)
#     print(d[21])
# print(dict.setdefault.__doc__)

# a = {}

print(d.get(21,441))
print(d)

