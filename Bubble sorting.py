#Harry Derouich
#09/01/15
#Bubble sort



def sorter(names):
    #changed = True
    #run = True
    #done = False
    #while run == True and done != True:
    for count in range(len(names)):
        for count in range(len(names) - 1):
            if str(names[count][0]) > str(names[count + 1][0]):
                temp = names[count]
                names[count] = names[count + 1]
                names[count + 1] = temp
                print(names)
                #changed = True
            else:
                names[count] = names[count]
                #changed = False
##        if changed == True:
##            run = True
##            changed = False
##        else:
##            run = True
##            done = False
                
                
    print("Finished")
    for name in names:
        print(name)
    return names




    

names = ['Frank','Emma','David','Charlie', 'Ben', 'Alex']
sorter(names)
#run_again(changed, names, sorted_names)
#print("List sorted!")
#for sorted_name in sorted_names:
   # print(sorted_name)

