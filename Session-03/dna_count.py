user_input = input("Enter a DNA sequence: ")

countA = 0
countC = 0
countG = 0
countT = 0

for element in user_input:
    if element == "A":
        countA += 1
    elif element == "C":
        countC += 1
    elif element == "G":
        countG += 1
    else:
        countT += 1

print("Total length: ", len(user_input))
print("A: ", countA)
print("C: ", countC)
print("T: ", countT)
print("G: ", countG)
