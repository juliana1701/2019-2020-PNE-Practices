import termcolor


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


def print_seqs(seq_list, colour):
    index = 0
    for sequences in seq_list:
        termcolor.cprint(f"sequence {index}: (Length: {sequences.len()}) {sequences}", colour)
        index += 1


seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
print_seqs(seq_list1, "blue")

print()
termcolor.cprint("List 2:", "green")
print_seqs(seq_list2, "green")
