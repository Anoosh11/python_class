import re

lesson_list=[]

def show_list():
    print("menu")
    print("1)Add lesson")
    print("2)show lesson list")
    print("3)find by teacher")
    print("0)exit")

    option = int(input("enter yor choice:"))
    return option

def code_checker(code):
    if code>=0:
        return True
    else:
        print("Error: invalid code!!!")
        return False

def title_checker(title):
    if re.match(r"^[a-z0-9\s]{3,30}$",title,re.I):
        return True
    else:
        print("Error: invalid title!!!")
        return False

def teacher_checker(teacher):
    if re.match(r"^[a-z\s]{3,30}$",teacher,re.I):
        return True
    else:
        print("Error: invalid teacher name!!!")
        return False

def day_checker(day):
    day_list=["sat","sun","mon","thu","wed"]
    if day in day_list:
        return True
    else:
        return False

def get_data():
    code = int(input("enter your lesson code:"))
    title = input("enter your lesson title:")
    teacher = input("enter your lesson teacher:")
    day = input("enter your lesson day:").lower()
    if code_checker(code) and title_checker(title) and teacher_checker(teacher) and day_checker(day):
        lesson={"code":code,"title":title,"teacher":teacher,"day":day}
        lesson_list.append(lesson)

def show_lesson_list():
    for lesson in lesson_list:
      print("lesson code:",lesson["code"],"lesson title:",lesson["title"],"lesson teacher:",lesson["teacher"],"lesson day:",lesson["day"])

def teacher_name_founder():
    teacher_name = input("enter your teacher name to search:")
    for lesson in lesson_list:
        if lesson["teacher"] == teacher_name:
           print("teacher name found")
        else:
            print("teacher name not found")




