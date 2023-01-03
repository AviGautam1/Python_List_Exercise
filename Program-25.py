# Write a python program to check whether two lists are circularly identical.


list1 = [8, 8, 12, 12, 8]
list2 = [8, 8, 8, 12, 12]
list3 = [1, 8, 8, 12, 12]

print("Compare List1 and List2 : " ,' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print("Compare List1 and List3 : " ,' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


'''
output = 
Compare List1 and List2 :  True
Compare List1 and List3 :  False
'''