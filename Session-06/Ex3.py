class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        for b in strbases:
            if b not in ["A", "C", "G", "T"]:
                self.strbases = "ERROR"
                print("ERROR!!")
                return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def generate_seqs(pattern, number):
    list_seqs = []
    for element in range(1, number + 1):
        sequence = Seq(pattern * element)
        list_seqs.append(sequence)
    return list_seqs


def print_seqs(seq_list):
    index = 0
    for sequences in seq_list:
        print(f"sequence {index}: (Length: {sequences.len()}) {sequences}")
        index += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
