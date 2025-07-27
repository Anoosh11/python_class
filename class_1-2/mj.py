name_list=[]
while True:
    name=input("enter your name: ").lower()
    if name == "exit":
        break
    name_list.append(name)
sum=0
for name in name_list:
    count_i=name.count("i")
    sum+=count_i
    count_j=name.count("j")
    sum+=count_j
    print("name is:",name," ","(i)is:",count_i," ","(j) is:",count_j)
print("total (i) and (j) is:",sum)