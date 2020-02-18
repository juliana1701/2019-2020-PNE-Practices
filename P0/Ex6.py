from Seq0 import *

FOLDER = "../Session-04/"
FILENAME = "U5.txt"
print("--- Exercise 6 ---")
print("Gene U5")
print("Frag: ", seq_read_fasta(FOLDER+FILENAME)[:20])
print("Rev: ", seq_reverse(seq_read_fasta(FOLDER+FILENAME)[:20]))
