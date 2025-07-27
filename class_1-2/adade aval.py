a=int(input( "adad ra vared konid : "))

count=0

for i in range(1,a+1):
    if a%i ==0:
        count+=1
    print(i,count)
if count==2:
    print("adad aval ast")
else:
    print("adad aval nist")
