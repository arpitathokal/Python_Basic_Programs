#. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

Sample_List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

Sample_List.remove('Red')
Sample_List.remove('Pink')
Sample_List.remove('Yellow')
print(Sample_List)