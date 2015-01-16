#Harry Derouich
#16/01/15
#Lists Stretch and challenge #1

def add_item(names):
    to_add = input("Please enter the name you wish to add to the end of the list: ")
    names.append(to_add)
    return names


def delete_name(names):
    to_delete = input("Please enter the name you wish to delete: ")
    names.remove(to_delete)
    return names


def delete_index(names):
    index = int(input("Please enter the index number of the name you wish to remove: "))
    names.pop(index - 1)
    return names

def insert_item(names):
    index_before = int(input("Please enter the position you wish to place the name before: "))
    name = input("Please enter the name you wish to insert: ")
    names.insert(index_before - 1, name)
    return names

def amend(names):
    index = int(input("Please enter the index number you wish to correct: "))
    print('You wish to change entry {0}, name: {1}'.format(index, names[index - 1]))
    ammendment = input("Please enter the correction: ")
    names[index - 1] = ammendment
    return names


def interface(names):
    for index, name in enumerate(names):
        print("{0}. {1}".format(index + 1, name))
    print('')
    print('1. Add a new item to the end of the list')
    print('2. Delete an item by name')
    print('3. Delete an item by list position')
    print('4. Insert a new item')
    print('5. Amend an item')
    print('9. Exit')
    option = int(input("Enter option: "))
    return option

def option_navigator(option, names):
    if option == 1:
        print("Add item")
        print('')
        names = add_item(names)
    elif option == 2:
        print("Delete by name")
        print('')
        names = delete_name(names)
    elif option == 3:
        print("Delete by name position")
        print('')
        names = delete_index(names)
    elif option == 4:
        print("Insert item")
        print('')
        names = insert_item(names)
    elif option == 5:
        print("Amend item")
        print('')
        names = amend(names)
    elif option == 9:
        print("Exiting Program")
    else:
        print("Please try again, enter a number correctly")
        #back to interface
    return names


names = ['Alex','Ben','Charlie','David','Elliot','Frank']
option = interface(names)
names = option_navigator(option, names)
print(names)
