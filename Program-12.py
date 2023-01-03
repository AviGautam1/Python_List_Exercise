# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

lst = [2, 4, 6, 7, 8, 1, 12, 22]
print("Original List : ", lst)

lst = [x for (i,x) in enumerate(lst) if i not in (0,4,5)]       # enumerate(iterable, start=0)
print("After Removing the 0th, 4th and 5th elements : ", lst)


'''
output = 
Original List :  [2, 4, 6, 7, 8, 1, 12, 22]
After Removing the 0th, 4th and 5th elements :  [4, 6, 7, 12, 22]
'''






