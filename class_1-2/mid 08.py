n=[]
a=0
b=1
for i in range(1,20):
    c=a+b
    a=b
    b=c
    n.append(a)
print(n)