#Harry Derouich
#09/01/15
#Linear Search

def get_info():
    names = ["Bob", "Ben", "Bill", "Frank", "James"]
    person = input("Search: ")
    return names, person

def search(names, person):
    count = 0
    found = False

    while not found and count < len(names):
        if names[count] == person:
            found = True
        else:
            found = False
        count = count + 1
    return found

def output(found):
    if found == True:
        print("User: '{0}' is Found".format(person))
    else:
        print("User: '{0}' is not found".format(person))
    



names, person = get_info()
found = search(names, person)
output(found)

