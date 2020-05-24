import http.client
import termcolor
import json

def menu ():
    print("1- List of species ")
    print("2- Karyotype")
    print("3- Chromosome length")
    print("4- Sequence of human gene")
    print("5- Information of human gene")
    print("6- length and percentage of basis")
    print("7- Sequence human gene")


def client(client_request, number_json):
    PORT = 8080
    SERVER = 'localhost'

    print(f"\nConnecting to server: {SERVER}:{PORT}\n")

    conn = http.client.HTTPConnection(SERVER, PORT)

    try:
        conn.request("GET", client_request + "&json=" + number_json)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data1 = r1.read().decode("utf-8")
    data = json.loads(data1)
    termcolor.cprint(f"CONTENT: {data}", "yellow")


options = True
while options:
    print("Client proving API rest")
    menu()
    option = int(input("Choose an option from menu: "))
    json_number = input("Enter a number for json: ")
    if option == 1:
        limit_parameter = input("Select the number of species: ")
        req = "/listSpecies?limit=" + limit_parameter
        client(req, json_number)
    elif option == 2:
        parameter = input("choose specie: ")
        req = "/karyotype?specie=" + parameter
        client(req, json_number)
    elif option == 3:
        specie_parameter = input("Choose specie: ")
        chromo_parameter = input("Choose chromosome: ")
        req = f"/chromosomeLength?specie={specie_parameter}&chromo={chromo_parameter}"
        client(req, json_number)

    elif option == 4:
        gene_parameter = input("Choose a human gene: ")
        req = "/geneSeq?gene=" + gene_parameter
        client(req, json_number)

    elif option == 5:
        gene_parameter = input("Choose a human gene: ")
        req = "/geneInfo?gene=" + gene_parameter
        client(req, json_number)

    elif option == 6:
        gene_parameter = input("Choose a human gene: ")
        req = "/geneCalc?gene=" + gene_parameter
        client(req, json_number)

    elif option == 7:
        chromo_parameter = input("Choose a human chromosome: ")
        start_point = input("Choose the start point: ")
        end_point = input("Choose the end point: ")
        req = f"/geneList?chromo={chromo_parameter}&start={start_point}&end={end_point}"
        client(req, json_number)

    elif option == 8:
        options = False
    else:
        print("Choose a valid option between 1-7 or 8 to exit the client")
