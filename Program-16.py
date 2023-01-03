'''
Write a Python program to generate and print a list except for the first 5 elements,
where the values are square of numbers between 1 and 30 (both included).
'''


lst = list()
for i in range(11, 25):
	lst.append(i**2)


print(lst[5:])

# output = [256, 289, 324, 361, 400, 441, 484, 529, 576]
