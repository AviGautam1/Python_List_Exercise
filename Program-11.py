# Write a Python function that takes two lists and returns True if they have at least one common member.


lst1 = [2, 4, 5, 6, 8, 1]
lst2 = [2, 5, 12, 6, 8]

def check(lst1, lst2):
    for x in lst1:
        for y in lst2:
            if x == y:
                return True
            else:
                return False


print(check(lst1, lst2))


# output = True