# Write a Python program to find the second smallest number in a list.


def second_smallest(lst):
    return sorted(set(lst))[1]
# We used the set() class to convert the list to a set to remove any duplicates.
# The sorted function returns a new sorted list from the items in the iterable.
# The last step is to access the list element at index 1.

print("Second Smallest Number Is : ", second_smallest([1, 4, 5, 7, 8, 12]))

# output = Second Smallest Number Is :  4

