class Seq:
    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL sequence created")
            return
        for b in strbases:
            if b not in ["A", "C", "G", "T"]:
                self.strbases = "ERROR"
                print("ERROR!!")
                return
        self.strbases = strbases
        print("New sequence created")

    def __str__(self):
        return self.strbases

    def len(self):
        if self.strbases == self.NULL:
            return 0
        elif self.strbases == self.ERROR:
            return 0
        else:
            return len(self.strbases)

    def count_base(self, base):
        counter = 0
        if self.strbases == self.NULL:
            return counter
        elif self.strbases == self.ERROR:
            return counter
        else:
            for element in self.strbases:
                if element == base:
                    counter += 1
            return counter, round((counter / self.len()) * 100, 1)

    def count(self):
        d = {"A": 0, "C": 0, "T": 0, "G": 0}
        if self.strbases == self.NULL:
            d = {"A": 0, "C": 0, "T": 0, "G": 0}
        elif self.strbases == self.ERROR:
            d = {"A": 0, "C": 0, "T": 0, "G": 0}
        else:
            for base in self.strbases:
                if base == "A":
                    d["A"] += 1
                elif base == "C":
                    d["C"] += 1
                elif base == "G":
                    d["G"] += 1
                else:
                    d["T"] += 1
        return d

    def reverse(self):
        if self.strbases == self.NULL:
            return self.strbases
        elif self.strbases == self.ERROR:
            return self.strbases
        else:
            return self.strbases[::-1]

    def complement(self):
        if self.strbases == self.NULL:
            return self.strbases
        elif self.strbases == self.ERROR:
            return self.strbases
        else:
            d = {"A": "T", "C": "G", "T": "A", "G": "C"}
            value = ""
            for element in self.strbases:
                value = value + d[element]
            return value

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        content = file_contents.split("\n")[1:]
        self.strbases = "".join(content)
        return self


def generate_seqs(pattern, number):
    list_seqs = []
    for element in range(1, number + 1):
        sequence = Seq(pattern * element)
        list_seqs.append(sequence)
    return list_seqs


def print_seqs(seq_list):
    index = 0
    for sequences in seq_list:
        index += 1
        print(f"sequence {index}: (Length: {sequences.len()}) {sequences}")
