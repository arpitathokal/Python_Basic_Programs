#1.Python program to interchange first and last elements in a list
# list=[1,2,54,13,'a',8]
# print(list)
# temp=list[0]
# list[0]=list[-1]
# list[-1]=temp
# print(list)


#2.Python program to swap two elements in a list
# list=[12,45,87,33,10,21]
# print(list)
# a=int(input("Enter first element you want to swap in list"))
# b=int(input("Enter second element you want to swap in list"))
# i=list.index(a)
# print(i)
# j=list.index(b)
# print(j)
# temp=list[i]
# list[i]=list[j]
# list[j]=temp
# print(list)

#3.	Python program to remove Nth occurrence of the given word

# Function to remove Ith word
# def RemoveIthWord(lst, word, N):
#     newList = []
#     count = 0
#
#     # iterate the elements
#     for i in lst:
#         if (i == word):
#             count = count + 1
#             if (count != N):
#                 newList.append(i)
#         else:
#             newList.append(i)
#
#     lst = newList
#
#     if count == 0:
#         print("Item not found")
#     else:
#         print("Updated list is: ", lst)
#
#     return newList
#
#
# # Driver code
# list = ["geeks", "for", "geeks"]
# word = "geeks"
# N = 2
#
# RemoveIthWord(list, word, N)


######################################################
