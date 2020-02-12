from Seq0 import *

folder = "../Session-04/"
list_seq = ["U5", "ADA", "FRAT1", "FXN", "U5"]
txt = ".txt"

for element in list_seq:
    dna_seq = seq_read_fasta(folder+element+txt)
    print("Gene", element, "--->", "Length:", seq_len(dna_seq))
