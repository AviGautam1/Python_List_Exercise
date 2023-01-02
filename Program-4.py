# Write a Python program to get the smallest number from a list.

list = [2, 4, 6, 7, 8, 12]
def smallest(list):
    small = list[0]
    for i in list:
        if i < small:
            small = i
    return small


print("Smallest Number Is : ", smallest(list))


# output = Smallest Number Is :  2