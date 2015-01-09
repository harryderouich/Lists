#Harry Derouich
#09/01/15
#Bubble sort



def sorter(names):
    print(names)
    changed = True
    while changed != False:
        for count in range(len(names) - 1):
            if str(names[count][0]) > str(names[count + 1][0]):
                temp = names[count]
                names[count] = names[count + 1]
                names[count + 1] = temp
                print(names)
                changed = True
            else:
                names[count] = names[count]
                changed = False
    return names




    

names = ['B','C','E','A', 'D', 'F']
sorted_names = sorter(names)
#run_again(changed, names, sorted_names)



