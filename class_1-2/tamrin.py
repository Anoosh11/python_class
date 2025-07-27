algorithm=0
number_list=[]
algorithm+=1

algorithm+=1
for i in range(100,1000,2):
    algorithm+=4
    if i %7 == 0:
        number_list.append(i)
average=sum(number_list)/len(number_list)
algorithm+=1

print("average is:",average,algorithm)
algorithm+=1
