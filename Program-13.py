# Write a Python program to print the numbers of a specified list after removing even numbers from it.

lst = [2, 4, 5, 3, 8]
print("Original List : ", lst)
lst2 = []

for i in lst:
    if (i % 2 != 0):
        #print(i)
        lst2.append(i)
    else:
        pass



print("List After Removing Even Numbers : ", lst2)


'''
output =
Original List :  [2, 4, 5, 3, 8]
List After Removing Even Numbers :  [5, 3]
'''



