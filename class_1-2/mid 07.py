A=[]
for i in range (100,1000):
    if i%7==0:
     A.append(i)
average=sum(A)/len(A)
print("average is:",average)
