from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"
PORT = 8080
test_sequence = "ACCGT"
# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
c.ping()

# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")

# TEST PING
print("* Testing PING...")
print(c.talk("PING"))

# TEST GET
print("* Testing GET...")
print("GET 0:", c.talk("GET 0"))
print("GET 1:", c.talk("GET 1"))
print("GET 2:", c.talk("GET 2"))
print("GET 3:", c.talk("GET 3"))
print("GET 4:", c.talk("GET 4"))

# TEST INFO
print("* Testing INFO...")
print(c.talk("INFO " + test_sequence))

# TEST COMP
print("* Testing COMP...")
print("COMP " + test_sequence)
print(c.talk("COMP " + test_sequence))

# TEST REV
print("* Testing GENE...")
files_list = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for file in files_list:
    print("GENE", file)
    print(c.talk("GENE " + file))
