from Seq1 import *

print("-----| Practice 1, Exercise 5 |------")

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_base = ["A", "C", "T", "G"]

print(f"Sequence 1: (Length: {s1.len()}) {s1}")
for base in list_base:
    print(base, ":", s1.count_base(base), end=", ")
print(f"\n Sequence 2: (Length: {s2.len()}) {s2}")
for base in list_base:
    print(base, ":", s2.count_base(base), end=", ")
print(f"\n Sequence 3: (Length: {s3.len()}) {s3}")
for base in list_base:
    print(base, ":", s3.count_base(base), end=", ")
