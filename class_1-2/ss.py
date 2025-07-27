wood_number_list=[]
print("1) Add wood")
print("2) wood list")
print("3) find best wood")
print("0) exit")
print()

while True:
    choice=int(input("enter your choice: "))
    print(40*"_")
    if  choice == 0:
         break

    elif choice==1:
        while True:
          wood = int(input("enter wood number: "))
          if wood == 0:
             print(40*"_")
             break
          if wood<0:
             print("wood number is out of range !!!")
          else:
             wood_number_list.append(wood)

    elif choice==2:
        wood_number_list.sort()
        print(wood_number_list)
        print(40*"_")
    elif choice==3:
        best_wood = int(input("enter your best wood number: "))
        for i in wood_number_list:
            if i == best_wood:
                print(i)
                break
            if i-best_wood >0:
                print(i)
                break
