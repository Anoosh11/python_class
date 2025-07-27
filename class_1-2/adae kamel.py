a=int(input( "enter number: "))

sum_number=0

for i in range(1,a):
    if a % i==0:
        sum_number+=i
if a == sum_number:
    print( "adad kamel ast ")
else:
    print( "adad kamel nist ")