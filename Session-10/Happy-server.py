import socket

IP = "212.128.253.139"
PORT = 8080

# --- Step 1: creating the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# --- Step 2: Bing the socket to the servers IP amd PORT
ls.bind((IP, PORT))

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# --- Step 3: Convert into a listening socket
ls.listen()

print("Server is configured")

while True:

    try:
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

        print(f"Received message: {msg}")

        # --- Step 5: Send a response message to the client
        response = "Hi, I am a happy server!"
        cs.send(response.encode())

        cs.close()
