# Write a Python program to sum all the items in a list.

# Using sum() Method Sum(iterable, start)
lst = [2, 3, 5, 6, 8, 12, 23]
lst_sum = sum(lst)
print("Sum Of List Is : ", lst_sum)

lst_sum = sum(lst, 2)
print("\nSum Of List Is : ", lst_sum)

'''
output = 
Sum Of List Is :  59
Sum Of List Is :  61
'''

# Using for Loop
lst = [2, 3, 5, 6, 8, 12, 23]
lst_sum = 0

for i in lst:
    lst_sum += i

print("Sum Of List Is : ", lst_sum)

# output = Sum Of List Is :  59
