# Program to search for a name in a list

NamesList = ['Jim', 'Bob', 'Alison', 'Jo', 'James']


ThisElement = 0
Found = False
while not Found:
    ElementSought = input('Enter the name you are searching for : ')
    if NamesList[ThisElement] == ElementSought:
        Found = True
    elif NamesList[ThisElement != ElementSought:
            print('Not found')
       else:
          ThisElement = ThisElement + 1

if Found:
   print('{0} was in element {1} in the list'.format(ElementSought, ThisElement + 1))
else:
   print('Not found')
