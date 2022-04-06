list1 = list(map(int, input("Enter Plot Registration No. :")))
k=int(input("Enter value of k: "))
print(list1)
i=0
list2=[]

while i<k:
    for j in list1:
        if j%2==0:
            list2.append(list1[2])
        else:
            list2.append(j)
    i=i+1
print(list2)


print(list1)
