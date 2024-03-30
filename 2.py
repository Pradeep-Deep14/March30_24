#List of Count of Elements

L=[1,1,2,2,3,3]
Element_Count={}

for element in L:
    if element in Element_Count:
        Element_Count[element]+=1
    else:
        Element_Count[element]=1

#print(Element_Count)
for element,count in Element_Count.items():
    print(f"The count of {element} is : {count}")