index1 = 0
index2 = 1

for number in range(0, 11):
    if number == 0:
        number = 0
        sumn = 0
    elif number == 1:
        sumn = 1
    else:
        sumn = index1 + index2
        index1 = index2
        index2 = sumn
    print(sumn, end=" ")
