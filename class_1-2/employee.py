from employee_module import *

while True:
    option=show_menu()

    if option == 1:
        get_data()

    elif option == 2:
        show_list()
        print("_"*40)

    elif option == 3:
        print("thank you")
        break

    else:
        print("Error:invalid option!!")
        print("_"*40)