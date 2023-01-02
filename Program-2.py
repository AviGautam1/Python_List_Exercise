# Write a Python program to multiply all the items in a list.

lst = [2, 3, 5, 6, 2]

def multply_lst(lst):
    total = 1
    for i in lst:
        total *= i
    return total


print("Multiplication Of List Is : ", multply_lst(lst))

# output = Multiplication Of List Is :  360
