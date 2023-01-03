# Write a Python program to find the list of words that are longer than n from a given list of words.


str = input("Enter A String : ")
n = int(input("Enter Value of n : "))

new_list = []
text = str.split(" ")
for x in text:
	if len(x) > n:
		new_list.append(x)


print("List Of Words : ", new_list)


'''
output = 
Enter A String : hii avinesh gautam how are you what are you doing
Enter Value of n : 4
List Of Words :  ['avinesh', 'gautam', 'doing']
'''