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

    def print_seqs(self, seq_list):
        index = 0
        for sequences in seq_list:
            index += 1
            print(f"sequence {index}: (Length: {strbases.len()}) {strbases}")


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]

seq_list.print_seqs(seq_list)
