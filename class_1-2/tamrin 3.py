print("1) Add wood:")
print("2) wood list:")
print("3) find best wood:")
print("0) exit")
wood_list=[]
while True:
    choice=int(input("enter your choice:"))
    print(30*"-")
    if choice == 0:
        break

    elif choice==1:
        while True:
         wood=int(input("enter your wood number:"))
         wood_list.append(wood)
         if wood == 0:
            print("-"*30)
            break

    elif choice==2:
        wood_list.sort()
        wood_list.pop(0)
        print(wood_list)
        print("_"*30)
    elif choice==3:
        best_wood=int(input("enter your best wood number:"))
        for i in wood_list:
            if i==best_wood:
                print(i)
                break
            if i-best_wood > 0:
                print(i)
                break
