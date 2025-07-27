from data_person_module import *

while True:
    option=show_menu()

    if option==1:
        person=get_data()

    elif option==2:
        national_code_searcher()

    elif option==3:
        show_list()

    elif option==0:
        print("thank you")
        break

    else:
        print("Error:enter valid option")
        print("_"*40)

