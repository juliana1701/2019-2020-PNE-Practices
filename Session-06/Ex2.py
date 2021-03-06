class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
        for b in strbases:
            if b not in ["A", "C", "G", "T"]:
                self.strbases = "ERROR"
                print("ERROR!!")
                return
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


# --- Main program ---
def print_seqs(seq_list):
    index = 0
    for sequences in seq_list:
        print(f"sequence {index}: (Length: {sequences.len()}) {sequences}")
        index += 1


seq_lists = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_lists)
