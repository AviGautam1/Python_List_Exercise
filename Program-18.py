# Write a Python program to get the difference between the two lists.


names1 = ["avinesh", "deepak", "ankur", "atul"]
names2 = ["avinesh", "harish", "anil"]

difference = list(set(names1) - set(names2))
print(difference)

# output = ['ankur', 'atul', 'deepak']