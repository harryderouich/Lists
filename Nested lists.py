#Harry Derouich
#06/01/15
#Presenting a table - Nested lists

def column_1_width(players):
    for count in range(len(players)):
        if len(players[count][0]) > 4:
            width_1 = len(players[count][0])
        else:
            width_1 = 4
    return width_1

def column_2_width(players):
    for count in range(len(players)):
        if len(players[count][1]) > 5:
            width_2 = len(players[count][1])
        else:
            width_2 = 5
    return width_2

def column_3_width(players):
    for count in range(len(players)):
        if len(players[count][2]) > 6:
            width_3 = len(players[count][1])
        else:
            width_3 = 6
    return width_3

def formatting(w_1, w_2, w_3):
    headings = ['Name', 'Kills', 'Deaths']
    print('|{0:>{3}}|{1:^{4}}|{2:^{5}}|'.format(headings[0], headings[1], headings[2], w_1, w_2, w_3))
    full_width = (w_1 + w_2 + w_3) + 4
    for count in range(len(players)):
        print('|{0:>13}|{1:^7}|{2:^9}|'.format(players[count][0], players[count][1], players[count][2]))
    print('-'* full_width)


players = [
    ['k1llmAchine', '51', '49'],
    ['bob2247', '5', '99'],
    ['hAx0r12', '72', '30']
]
##
##
##print('-'*33)
##print('|{0:>13}|{1:^7}|{2:^9}|'.format(headings[0], headings[1], headings[2]))
##print('|'+('-'*13)+'|'+('-'*7)+'|'+('-'*9)+'|')
##
##for count in range(len(players)):
##    print('|{0:>13}|{1:^7}|{2:^9}|'.format(players[count][0], players[count][1], players[count][2]))
##
##print('-'*33)

w_1 = column_1_width(players)
w_2 = column_2_width(players)
w_3 = column_3_width(players)
formatting(w_1, w_2, w_3)

