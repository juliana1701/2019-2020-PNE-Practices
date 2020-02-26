from Seq1 import *

print("-----| Practice 1, Exercise 9 |------")

FOLDER = "../Session-04/"
TXT = ".txt"
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.read_fasta(FOLDER + "U5" + TXT)

print(f"Sequence 1: (Length: {s.len()}) {s}")
print(f"Bases: {s.count()}")
print(f"Rev: {s.reverse()}")
print(f"Comp: {s.complement()}")
