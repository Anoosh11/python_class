A=[]
while True:
    n=int(input("enter number:"))
    A.append(n)
    if n == 0:
        break
average=sum(A)/len(A)
print("average is:",average)
