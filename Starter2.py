#Harry Derouich
#12/12/14
#Lists Starter Exercises

values = ["test", 24, 13, 57, 45]

result = 0
index = 0
while index != 4:
    index = index + 1
    if result < values[index]:
        result = values[index]
    print("Index: {0}, Result: {1}".format(index, result))

print("Final result is: ", result)
