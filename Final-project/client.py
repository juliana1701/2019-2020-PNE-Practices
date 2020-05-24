import http.client


def menu ():
    print("1- List of species ")
    print("2- Karyotype")
    print("3- Chromosome length")
    print("4- Sequence of human gene")
    print("5- Information of human gene")
    print("6- length and percentage of basis")
    print("7- Sequence human gene")


def client(client_request):
    PORT = 8080
    SERVER = 'localhost'

    print(f"\nConnecting to server: {SERVER}:{PORT}\n")

    conn = http.client.HTTPConnection(SERVER, PORT)

    try:
        conn.request("GET", client_request + "&json=1")
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    print(f"CONTENT: {data1}")


options = True
while options:
    print("Client for priving API rest")
    menu()
    option = int(input("Choose an option from menu"))

    if option == 1:
        limit_parameter = input("Select the number of species: ")
        req = "/listSpecies?limit=" + limit_parameter
        client(req)
    elif option == 2:
        parameter = input("choose specie: ")
        request = "/karyotype?specie=" + parameter
        client(request)

