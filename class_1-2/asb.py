n=int(input("enter no of products : "))
m=n**(1/2)
m=int(m)
l=0
for i in range (2,m+1):
    if n%i==0:
        l+=1
    if l==m-1:
        print('afarin')
