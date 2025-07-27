mos=0
loz=0
moteva=0

mos+=1
l=[]

mos+=1
for i in range(100,999,2):
    loz+=1
    mos+=2
    l.append(i)

mos+=1
average=sum(l)/len(l)
moteva+=1
print("average is : ",average)

print("moteva is : ",moteva)
print("mos is :",mos)
print("loz is : ",loz)
