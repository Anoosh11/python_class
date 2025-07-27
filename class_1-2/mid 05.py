names_list=[]
while True:
    n=input(" enter name:")
    names_list.append(n)
    if len(names_list)>10:
        break
names_list.reverse()
print(names_list)
