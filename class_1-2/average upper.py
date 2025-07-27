number_list=[]
upper_avrg_list=[]
for i in range (10):
    n=int(input( " enter a number : "))
    number_list.append(n)
average=sum(number_list)/len(number_list)
print(average)
for numb in number_list:
    if numb>average:
        upper_avrg_list.append(numb)
print(upper_avrg_list)

