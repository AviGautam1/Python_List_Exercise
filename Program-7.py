# Write a Python program to remove duplicates from a list.

# Using set()  Set cannot have a duplicate item in it.

lst = [1, 2, 3, 3, 4, 5, 4, 1, 8, 7, 8]
print("After Removing Duplicates : ", set(lst))
print("After Removing Duplicates : ", list(set(lst)))       # we first convert the list into a set, then we again convert it into a list.


'''
output = 
After Removing Duplicates :  {1, 2, 3, 4, 5, 7, 8}
After Removing Duplicates :  [1, 2, 3, 4, 5, 7, 8]
'''