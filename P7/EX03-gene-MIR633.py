import http.client
import json
import termcolor
from Seq1 import Seq

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
params = '?content-type=application/json'
gene = "ENSG00000207552"
URL = server + endpoint + gene + params

print(f"\nConnecting to server: {server}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + gene + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

response = json.loads(data1)


termcolor.cprint("Gene", 'green', end="")
print(f": MIR633")
termcolor.cprint("Description", 'green', end="")
print(f": {response['desc']}")
termcolor.cprint("Bases", 'green', end="")
print(f": {response['seq']}")

gene_seq = Seq(response["seq"])
