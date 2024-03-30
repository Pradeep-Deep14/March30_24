#Print the duplicates in the List

L1=[1,2,2,3,4,5]

Duplicates=[x for x in L1 if L1.count(x)>1]
print(Duplicates)