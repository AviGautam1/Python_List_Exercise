# Write a Python program to shuffle and print a specified list.


from random import shuffle

emp_name = ["avinesh", "sandeep", "priyanka", "abhi"]
print("Original List : ", emp_name)
shuffle(emp_name)

print("After Shuffle List : ", emp_name)


'''
output = 
Original List :  ['avinesh', 'sandeep', 'priyanka', 'abhi']
After Shuffle List :  ['priyanka', 'abhi', 'sandeep', 'avinesh']
'''