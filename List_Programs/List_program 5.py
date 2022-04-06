# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

Sample_List = ['abc', 'xyz', 'aba', '1221','67676']
count=0
for x in Sample_List:
    if len(x)>2 and x[0]==x[-1]:
       count+=1
print(count)