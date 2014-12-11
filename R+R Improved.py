#Harry Derouich
#Improved Code - R+R

def get_names():
    test = 0
    name1 = input("Please enter the first students name: ")
    name2 = input("Please enter the second students name: ")
    name3 = input("Please enter the third students name: ")
    name4 = input("Please enter the fourth students name: ")
    name5 = input("Please enter the fifth students name: ")
    name6 = input("Please enter the sixth students name: ")
    name7 = input("Please enter the seventh students name: ")
    name8 = input("Please enter the eighth students name: ")
    test = 0
    return test, name1, name2, name3, name4, name5, name6, name7, name8
    



def all_names(test, name1, name2, name3, name4, name5, name6, name7, name8):
    students = [test, name1, name2, name3, name4, name5, name6, name7, name8]
    return students


def table(end,name1,name2,name3,name4,name5,name6,name7,name8):   
    Students = [end,name1,name2,name3,name4,name5,name6,name7,name8]
    count = (0)
    for each in Students:
        print("{0}. {1}".format(count, each))
        count = count+(1)

name1,name2,name3,name4,name5,name6,name7,name8 = get_names()
table(name1,name2,name3,name4,name5,name6,name7,name8)
