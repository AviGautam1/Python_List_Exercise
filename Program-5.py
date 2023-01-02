'''
Write a Python program to count the number of strings where the string length is 2 or more and the
first and last character are same from a given list of strings.
'''

str = ['abc', 'xyz', 'aba', '1221']
def check(str):
    character = 0
    for i in str:
        if len(i) > 1 and i[0] == i[-1]:
            character += 1
    return character


print("Character Is : ", check(str))


# output = Character Is :  2

