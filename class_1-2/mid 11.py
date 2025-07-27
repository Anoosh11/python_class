a=int(input("enter score 1: "))
b=int(input("enter score 2: "))
c=int(input("enter score 3: "))
count=0
sum_number=0
while a>0 and b>0 and c>0:
      count=count+1
      sum_number=sum_number+a+b+c
average=sum_number/count
    print("average is:",average)
if a>b and a>c:
     print("a is greater than b")
if b>a and b>c:
     print("b is greater than c")
else:
     print("c is greater than c")