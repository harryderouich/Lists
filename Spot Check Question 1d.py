#Harry Derouich
#20/01/15
#Lists Spot Check - Question 1d


scores = [18,23,36,21,58,40,45,59]
max = 8

for count in range(max - 1):
    if scores[count] > scores[count + 1]:
        temp = scores[count]
        scores[count] = scores[count + 1]
        scores[count + 1] = temp


for index in range(len(scores)):
    print('{0}. {1}'.format(index + 1, scores[index]))
          
