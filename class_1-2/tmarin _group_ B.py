from group_B_module import *

while True:
    option=show_list()
    print("_"*40)

    if option == 1:
        lesson=get_data()

    elif option == 2:
        print("show lesson list")
        show_lesson_list()
        print("_"*40)

    elif option == 3:
        teacher_name_founder()
        print("_"*40)

    elif option == 0:
        print("thank you")
        break

    else:
        print("Error: invalid choice!!!")

        print("_" * 40)