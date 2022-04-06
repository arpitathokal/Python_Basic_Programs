#Write a Python program to clone or copy a list.
#Write a Python program to get the largest number from a list.

Sample_List=[2,12,65,77]
temp=[]
for x in Sample_List:
    if x not in temp:
        temp.append(x)
for i in Sample_List:
    for j in temp:
        if Sample_List[i]>temp[j]:
            print(Sample_List[i])



