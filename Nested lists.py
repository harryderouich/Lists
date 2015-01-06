#Harry Derouich
#06/01/15
#Presenting a table - Nested lists
headings = ['Name', 'Kills', 'Deaths']

players = [
    ['k1llmAchine', '51', '49'],
    ['bob2247', '5', '99'],
    ['hAx0r12', '72', '30']
]



print('|{0:>13}|{1:^7}|{2:^9}|'.format(headings[0], headings[1], headings[2]))
print('|-------------|-------|---------|')

for count in range(len(players)):
    print('|{0:>13}|{1:^7}|{2:^9}|'.format(players[count][0], players[count][1], players[count][2]))
