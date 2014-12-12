#Harry Derouich
#12/12/14
#Lists Starter Exercises

shopping_list = []
finished = False

while not finished:
    shopping_item = input("Enter next item (-1 to end list): ")
    if shopping_item == "-1":
        finished = True
    else:
        shopping_list.append(shopping_item) #add new item to the list

item = "Item"
print("|Item #|{0:^10}|".format(item))
print("|------|----------|")
for index in range(len(shopping_list)):
    print("|{0:^6}|{1:^10}|".format(index+1, shopping_list[index]))
