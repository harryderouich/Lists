#Harry Derouich
#Lists Class Exercises - Development 1

import random

countries = ['England','France','Germany','Spain','Portugal','Italy','USA','South Africa', 'Australia', 'Scotland']
print(countries)
capitals = ['London', 'Paris', 'Berlin', 'Madrid', 'Lisbom', 'Rome', 'Washington D.C.', 'Cape Town', 'Canberra', 'Glasgow']
print(capitals)

number = random.randint(0,10)
print(number)

answer = (input("What is the capital of: {0}? - ".format(countries[number])))

if answer == capitals[number]:
    print('Correct, the capital of {0} is {1}'.format(countries[number], capitals[number]))
else:
    print("Incorrect, the capital of {0} is {1}".format(countries[number], capitals[number]))

    

