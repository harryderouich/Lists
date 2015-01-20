#Harry Derouich
#20/01/15
#Lists Spot Check - Question 2g

import random

def array():
    frequency = [0,0,0,0,0,0]
    return frequency

def dice_throw(frequency):
    for count in range(20):
        result = random.randint(1,6)
        frequency[result - 1] = frequency[result - 1] + 1
    return frequency

def display_result(frequency):
    print('Dice Roll Results')
    print('')
    titles = ['Score','Frequency']
    print('{0:^7} {1:^11}'.format(titles[0],titles[1]))
    for count in range(6):
        print('{0:^7} {1:^11}'.format(count + 1, frequency[count]))

def freq_dice_rolls():
    frequency = array()
    frequency = dice_throw(frequency)
    display_result(frequency)

freq_dice_rolls()
