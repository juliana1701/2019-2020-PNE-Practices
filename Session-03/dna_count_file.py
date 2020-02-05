with open("dna.txt", "r") as f:
    countA = 0
    countC = 0
    countG = 0
    countT = 0
    total_count = 0
    for line in f:
        for character in line:
            total_count += 1
            if character == "A":
                countA += 1
            elif character == "C":
                countC += 1
            elif character == "G":
                countG += 1
            else:
                countT += 1

print("Total length: ", total_count)
print("A: ", countA)
print("C: ", countC)
print("T: ", countT)
print("G: ", countG)
