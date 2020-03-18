import socket
from Seq1 import Seq
import termcolor

IP = "127.0.0.1"
PORT = 8080
list_bases = ["A", "C", "G", "T"]
list_number = ["ACCGT\n", "ACTGA\n", "CTA\n", "TGCA\n", "TTA\n"]
folder = "../Session-04/"
s1 = Seq()

# --- Step 1: creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 2: Bing the socket to the servers IP amd PORT
ls.bind((IP, PORT))

# --- Step 3: Convert into a listening socket
ls.listen()

print("Seq-server is configured")

while True:

    try:
        print("Waiting for clients...")
        # --- Step 4: Wait for clients to connect
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server is done!")
        ls.close()
        exit()

    else:
        # --- Step 5: Receiving information from the client
        msg_raw = cs.recv(2000)
        msg = msg_raw.decode()
        command = msg[msg.find(" ") + 1:]

        # --- Step 5: Send a response message to the client
        if msg == "PING":
            termcolor.cprint("PING command", "green")
            response = "OK!\n"
            cs.send(response.encode())
            print(response)
        elif msg.startswith("GET"):
            termcolor.cprint("GET", "green")
            index = 0
            for element in list_number:
                if msg[4] == str(index):
                    cs.send(element.encode())
                    print(element)
                index += 1

        elif msg.startswith("INFO"):
            termcolor.cprint("INFO", "green")
            sequence = Seq(msg[5:])
            print(f"sequence: {sequence}")
            cs.send(str(sequence).encode())
            print(f"total length: {sequence.len()}")
            for base in list_bases:
                print(f"{base}: {sequence.count_base(base)} ({round(sequence.count_base(base) / sequence.len() * 100, 2)} %)")
                # respond = ("Sequence: " + str(sequence) + "\n" + "Total length: " + str(sequence.len()) + "\n" + sequence.count_base(base))
                # cs.send(respond.encode())

        elif msg.startswith("COMP"):
            sequence = Seq(msg[5:])
            print(sequence.complement() + "\n")
            cs.send(str(sequence.complement()).encode())

        elif msg.startswith("REV"):
            sequence = Seq(msg[4:])
            print(sequence.reverse() + "\n")
            cs.send(str(sequence.reverse()).encode())

        elif msg.startswith("GENE"):
            termcolor.cprint("GENE", "green")
            sequence = msg[5:]
            gene = s1.read_fasta(folder + sequence + ".txt")
            print(gene)
            cs.send(str(gene).encode())

        cs.close()
