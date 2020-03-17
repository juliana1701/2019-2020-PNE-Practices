from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT1 = 8080
PORT2 = 8081

# -- Create a client object
folder = "../Session-04/"
c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
s = Seq()
sequence = s.read_fasta(folder + "FRAT1.txt")
sequence = str(sequence)
fragment1 = sequence[0:10]
fragment2 = sequence[10:20]
fragment3 = sequence[20:30]
fragment4 = sequence[30:40]
fragment5 = sequence[40:50]
fragment6 = sequence[50:60]
fragment7 = sequence[60:70]
fragment8 = sequence[70:80]
fragment9 = sequence[80:90]
fragment10 = sequence[90:100]
fragment_list = [fragment1, fragment2, fragment3, fragment4, fragment5, fragment6, fragment7, fragment8, fragment9, fragment10]

# -- Send a message to the server
c1.talk(f"sending FRAT1 Gene to the server, in fragments of 10 bases...")
c2.talk(f"sending FRAT1 Gene to the server, in fragments of 10 bases...")
index_server = 0
for element in fragment_list:
    if (index_server + 1) % 2 == 0:
        c2.talk(f"Fragment {index_server +1}: {fragment_list[index_server]}")
        index_server += 1
    else:
        c1.talk(f"Fragment {index_server +1}: {fragment_list[index_server]}")
        index_server += 1

index = 0
for element in fragment_list:
    print(f"fragment {index + 1}: {fragment_list[index]}")
    index += 1
