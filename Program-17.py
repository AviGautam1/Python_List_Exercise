# Write a Python program to generate all permutations of a list in Python.


import itertools

list1 = [5, 12, 15]

perm = list(itertools.permutations(list1))

print(perm)


# output = [(5, 12, 15), (5, 15, 12), (12, 5, 15), (12, 15, 5), (15, 5, 12), (15, 12, 5)]