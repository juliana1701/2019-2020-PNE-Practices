class Seq:
    """A class for representing sequence objects"""
    def __init__(self, strbases):
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
        return len(self.strbases)


class Gene(Seq):
    pass


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")
