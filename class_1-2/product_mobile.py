from product_mobile_v1 import *

while True:
    option=show_menu()

    if option==1:
        mobile=get_data()


    elif option==2:
        code_finder()



    elif option==3:
        price_finder()

    elif option==4:
        print("show list ")
        show_list()

    elif option==0:
        break

    else:
        print(" Error: invalid option!!")

    print("_"*40)