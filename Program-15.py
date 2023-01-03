'''
Write a Python program to generate and print a list of first and last 5 elements where
the values are square of numbers between 1 and 30 (both included).
'''


lst = list()
for i in range(11, 25):
	lst.append(i**2)
print(lst[:5])
print(lst[-5:])


'''
output = 
[121, 144, 169, 196, 225]
[400, 441, 484, 529, 576]
'''