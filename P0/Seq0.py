def seq_ping():
    print("OK!")


def seq_read_fasta(filename):
    from pathlib import Path

    file_contents = Path(filename).read_text()

    content = file_contents.split("\n")[1:]
    body_file = ",".join(content).replace(",", "")
    return body_file


def seq_len(seq):
    counter = 0
    for element in seq:
        counter += 1
    return counter


def seq_count_base(seq, base):
    count_base = 0
    for element in seq:
        if element == base:
            count_base += 1
    return count_base


def seq_count(seq):
    d = {"A": 0, "C": 0, "T": 0, "G": 0}
    for bases in seq:
        if bases == "A":
            d["A"] += 1
        elif bases == "C":
            d["C"] += 1
        elif bases == "G":
            d["G"] += 1
        else:
            d["T"] += 1
    return d
