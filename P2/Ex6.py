from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8081

# -- Create a client object
folder = "../Session-04/"
c = Client(IP, PORT)
s = Seq()
sequence = s.read_fasta(folder + "FRAT1.txt")
sequence = str(sequence)

# -- Send a message to the server
c.talk(f"sending FRAT1 Gene to the server, in fragments of 10 bases...")
c.talk(f"fragment 1: {sequence[0:10]}")
c.talk(f"Fragment 2: {sequence[10:20]}")
c.talk(f"Fragment 3: {sequence[20:30]}")
c.talk(f"Fragment 4: {sequence[30:40]}")
c.talk(f"Fragment 5: {sequence[40:50]}")

print(f"fragment 1: {sequence[0:10]}")
print(f"Fragment 2: {sequence[10:20]}")
print(f"Fragment 3: {sequence[20:30]}")
print(f"Fragment 4: {sequence[30:40]}")
print(f"Fragment 5: {sequence[40:50]}")