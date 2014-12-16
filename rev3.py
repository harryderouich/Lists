#Harry Derouich
#16/12/14
#Lists Class Exercises - Revision 3
total = 0
weekly_temperature = [20.7, 23.4, 24.5, 24, 23.8, 19.7, 20.1]
for count in range(len(weekly_temperature)):
    total = total + weekly_temperature[count]

average = round(total / len(weekly_temperature), 2)
print(weekly_temperature)
print("The average is: {0}°C".format(average))
