#1. Write a Python program to sum all the items in a list.
#2. Write a Python program to multiplies all the items in a list
#3. Write a Python program to get the largest number from a list.
#4. Write a Python program to get the smallest number from a list.


# n = int(input("Enter the number of items in the list: "))
# i=1
# #sum = 0
# product = 1
# mylist=[]
# while i<=n:
#     x=int(input("Enter Number"))
#     mylist.append(x)
#     i=i+1
#     y= sum(mylist)
#     #sum = sum + x
#     product = product*x
# print("List =", mylist)
# print("Sum =", y)
# print("Product =", product)
# print("Maximum number =", max(mylist))
# print("Minimum number =", min(mylist))


#5.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2

# List1 = ['abc', 'xyz', 'aba', '1221']
# i=0
# for x in List1:
#     if(len(List1)>=2 and x[0]==x[-1]):
#         print(x)
#         i=i+1
# print(i)


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# mylist =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(mylist)-1):
#     for j in range(len(mylist)-1):
#         if mylist[j][1]>mylist[j+1][1]:
#             t=mylist[j]
#             mylist[j]=mylist[j+1]
#             mylist[j+1]=t
# print(mylist)


#7. Write a Python program to remove duplicates from a list.

# mylist = [12,32,11,5,12,3,67,32]
# print(mylist)
# temp =[]
# for x in mylist:
#     if x not in temp:
#         temp.append(x)
#     print(temp)

#8. Write a Python program to check a list is empty or not.
# list1=[12,32,'sra',2]
# list2=[]
# if len(list2)==0:
#     print("List is empty")
# else:
#     print("Not Empty")


#9. Write a Python program to clone or copy a list.
# list1=[10,20,30,40,50]
# print(list1)
# list2=list1.copy()
# print(list2)


# 10.Write a Python program to find the list of words that are longer than n from a given list of words.
# s1= "The quick brown fox jumps over the lazy dog"
# print(s1)
# n=int(input("Enter the value for n:"))
# x=s1.split()
# temp =[]
# for i in x:
#     if len(i)>n:
#         temp.append(i)
# print(temp)

#11. Write a Python function that takes two lists and returns True if they have at least one common member.
# list1 = [1,2,3,4,5]
# list2 = [9,6,7,8,0]
# result = False
# for x in list1:
#     for y in list2:
#         if x==y:
#           result=True
# print(result)


# <------------------------------------------------------------------>
#12.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# # color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
# color.remove('Red')
# print(color)
# <----------------------------------------------------------------------->


# 13.
# array = [[ ['*' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)
#
