L1=[1,2,3,4,5] 
L2=[1,2,2,3,4]

def has_unique_elements(lst):
    return len(lst)==len(set(lst))

print(has_unique_elements(L1))
print(has_unique_elements(L2))
