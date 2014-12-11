#Harry Derouich
#Lists R+R Exercises

def get_info():
    zero = "0"
    name1 = input("Please enter the name of student one: ")
    name2 = input("Please enter the name of student two: ")
    name3 = input("Please enter the name of student three: ")
    name4 = input("Please enter the name of student four: ")
    name5 = input("Please enter the name of student five: ")
    name6 = input("Please enter the name of student six: ")
    name7 = input("Please enter the name of student seven: ")
    name8 = input("Please enter the name of student eight: ")
    namelist = [zero, name1, name2, name3, name4, name5, name6, name7, name8]
    return namelist


def print_list(namelist):
    for count in range(1,9):
        print("{0}. {1}".format(count, namelist[count]))

def change_name(namelist):
    change = int(input("Please enter the student you wish to change: "))
    print("You wish to change '{0}'".format(namelist[change]))
    change_to = input("Enter name you wish to change to: ")
    namelist.pop(change)
    namelist.insert(change, change_to)

namelist = get_info()
print_list(namelist)
change_name(namelist)
print_list(namelist)




