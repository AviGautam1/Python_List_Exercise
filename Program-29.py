# Write a Python program to get the frequency of the elements in a list.


import collections

lst = [11, 12, 11, 12, 23, 24, 23, 24]
print("Original List Is : ", lst)

def count_freq(lst):
    return collections.Counter(lst)

freq = count_freq(lst)

print("Frequency of the elements in the List : ", freq)


'''
output = 
Original List Is :  [11, 12, 11, 12, 23, 24, 23, 24]
Frequency of the elements in the List :  Counter({11: 2, 12: 2, 23: 2, 24: 2})
'''