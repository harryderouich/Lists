#Harry Derouich
#06/01/15
#Extending the nested lists exercise

def table():
    list = [
        ['x',10,20,30,40],
        ['y',50,60,70,80],
        ['z',90,93,95,97]
    ]
    rows = len(list)
    columns = len(list[0])
    headers = ['Name','Kills','Deaths']
    namelength = 0
    killslength = 0
    deathslegth = 0
    for count in range(rows):
        if len(list[count][0]) > namelength:
            namelength = len(list[count][0])
    #do for each of the headings ^^
            
    

table()
    
