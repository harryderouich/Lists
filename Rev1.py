#Harry Derouich
#16/12/14
#Lists Class Exercises - Revision 1

print('Name List Generator')
names = []
for count in range(1,7):
    name = input("Please enter name #{0}: ".format(count))
    names.append(name)

counter = 1
for name in names:
    print("Name #{0}: {1}".format(counter, name))
    counter = counter + 1

##from_names = int(input("Please enter the range that you want to view FROM: "))
##to_names = int(input("Please enter the range that you want to view TO: "))
##print(names[from_names, to_names])
