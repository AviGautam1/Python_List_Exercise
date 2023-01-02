# Write a Python program to get the largest number from a list.

# Method-1
lst = [2, 5, 7, 12, 34, 56]
largest_num = lst[0]

for number in lst:
    if number > largest_num:
        largest_num = number


print("Largest Number Is : ", largest_num)

# output = Largest Number Is :  56


# Method-2
a = []
n = int(input("Enter number of elements : "))
for i in range(1,n+1):
    b = int(input("Enter element : "))
    a.append(b)
a.sort()

print("Largest element is:", a[n-1])

'''
output = 
Enter number of elements : 4
Enter element : 12
Enter element : 23
Enter element : 56
Enter element : 22
Largest element is: 56
'''