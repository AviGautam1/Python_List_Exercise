# Write a Python program to check a list is empty or not.


# using len()
lst = []

if len(lst) == 0:
    print("List Is Empty")

else:
    print("List Is Not Empty : ", lst)


# output = List Is Empty


# Using Boolean operation
lst = [1, 2, 4, 6]
if not lst:
    print("List Is Empty")

else:
    print("List Is Not Empty : ", lst)


# output = List Is Not Empty :  [1, 2, 4, 6]