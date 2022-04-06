# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for x in range(len(Sample_List)-1):
    for y in range(len(Sample_List)-1):
        if Sample_List[y][1]>Sample_List[y+1][1]:
            t=Sample_List[j]
            


