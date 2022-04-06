#Write a Python program to check a list is empty or not.
n=int(input("Enter the no. of element in the list:"))
Sample_list=[]
i=0
while i<n:
    x=input("Enter the element in list: ")
    Sample_list.append(x)
    i=i+1

print(Sample_list)
if len(Sample_list)==0:
    print("List is Empty")
else:
    print("List Not Empty")