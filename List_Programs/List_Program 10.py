#Write a Python program to find the list of words that are longer than n from a given list of words.

list1=['cat','dog','Mango','to','there']
print((list1))
n=int(input("Enter N: "))
for x in list1:
        if len(x)>n:
            print(x)
