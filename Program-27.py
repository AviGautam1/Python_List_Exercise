# Write a Python program to find the second largest number in a list.


# Method-1
lst = [12, 34, 45, 56, 76, 75]

lst.sort()      # sort the list

print("Second Largest Number Is : ", lst[-2])

# output = Second Largest Number Is :  75


# Method-2
lst = []
n = int(input("Enter the number of elements : "))
for i in range(1, n+1):
    elem = int(input("Enter the elements : "))
    lst.append(elem)
lst.sort()
print("The sorted List : ",lst)
print("The second largest value of sorted list : ",lst[n-2])


'''
output = 
Enter the number of elements : 10
Enter the elements : 12
Enter the elements : 13
Enter the elements : 14
Enter the elements : 15
Enter the elements : 16
Enter the elements : 17
Enter the elements : 18
Enter the elements : 20
Enter the elements : 23
Enter the elements : 45
The sorted List :  [12, 13, 14, 15, 16, 17, 18, 20, 23, 45]
The second largest value of sorted list :  23
'''