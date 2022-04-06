#Write a Python function that takes two lists and returns True if they have at least one common member.
list1=[]
n1=int(input("Enter no. of element in list1: "))
i=0
while i<n1:
    n=input("Enter element in list1: ")
    list1.append(n)
    i+=1
print(list1)

list2=[]
n2=int(input("Enter no. of element in list2: "))
j=0
while j<n2:
    a=input("Enter element in list2: ")
    list2.append(a)
    j+=1
print(list2)

for x in list1:
    for y in list2:
        if x==y:
            print("True")
