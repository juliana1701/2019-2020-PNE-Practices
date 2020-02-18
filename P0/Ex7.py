from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
print("--- Exercise 7 ---")
print("Gene U5")
print("Frag: ", seq_read_fasta(FOLDER+FILENAME)[:20])
print("Comp:", seq_complement(seq_read_fasta(FOLDER+FILENAME)[:20]))
