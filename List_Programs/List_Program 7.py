#Write a Python program to remove duplicates from a list.
Sample_List=[2,3,5,6,3,2,1,7]
temp=[]
for x in Sample_List:
    if x not in temp:
        temp.append(x)
print(temp)
        