import socket
import Seq1
import termcolor

IP = "127.0.0.1"
PORT = 8082
list_number = ["AC\n", "ACTGA\n", "CTA\n", "TGCA\n", "TTA\n"]

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

        cs.close()
