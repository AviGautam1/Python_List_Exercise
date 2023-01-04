# Write a Python program to get unique values from a list.

lst = [12, 13, 14, 12, 14, 15, 16, 12, 16]
print("Original List : ", lst)
lst1 = set(lst)         # convert list to set. set use to remove duplicate values
lst2 = list(lst1)       # convert set to list again.

print("Unique values from a list is : ", lst2)


'''
output =
Original List :  [12, 13, 14, 12, 14, 15, 16, 12, 16]
Unique values from a list is :  [12, 13, 14, 15, 16]
'''