list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
a=[]
b=[]
for i in list1:
    if i not in list2:
        a.append(i)
a.append(list2)
print(a)