from Seq0 import *

folder = "../Session-04/"
list_seq = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
txt = ".txt"
list_base = ["A", "C", "T", "G"]
print("--- Exercise 4 ---")
for element in list_seq:
    dna_seq = seq_read_fasta(folder+element+txt)
    print("Gene", element)
    for base in list_base:
        print(base, ":", seq_count_base(dna_seq, base))
