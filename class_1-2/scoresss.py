overall_list=[]
average_list=[]
for i in range (5):
    student=input("enter your name: ")
    while input("add your lesson ? YES/NO : ") == "yes".lower():
        lesson=input("enter your lesson name :")
        score=int(input("enter your score :"))
        average_list.append(score)
        average=sum(average_list)/len(average_list)

        overall={"name: ":student,"lesson: ":lesson,"average= ":average}
        overall_list.append(overall)
    else :
        print("-"*30)

for i in range(len(overall_list)):
      print(overall_list[i])
