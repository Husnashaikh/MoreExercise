a=["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
i=0
b=[]
c=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
print(b)
