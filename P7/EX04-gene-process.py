import http.client
import json
import termcolor
from Seq1 import Seq

list_bases = ["A", "C", "G", "T"]
genes = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839',
        'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379',
        'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296',
        'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078',
        'KDR': 'ENSG00000128052',
        'ANK2': 'ENSG00000145362',}

server = 'rest.ensembl.org'
endpoint = '/sequence/id/'
params = '?content-type=application/json'
gene_input = input("Write the gene name: ")
URL = server + endpoint + genes[gene_input] + params

print(f"\nServer: {server}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + genes[gene_input] + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

response = json.loads(data1)

print(response)

termcolor.cprint("Gene", 'green', end="")
print(f": {gene_input}")
termcolor.cprint("Description", 'green', end="")
print(f": {response['desc']}")
termcolor.cprint("Bases", 'green', end="")
print(f": {response['seq']}")

gene_seq = Seq(response["seq"])
seq = gene_seq.len()
termcolor.cprint("Total lengh", 'green', end="")
print(f": {seq}")

counter = 0
for element in list_bases:
    termcolor.cprint(f"{element}:", "blue", end="")
    print(f"{gene_seq.count_base(element)[0]} ({gene_seq.count_base(element)[1]}%)")

    if gene_seq.count_base(element)[0] > counter:
        counter = gene_seq.count_base(element)[0]
        freqbase = element

termcolor.cprint(f"Most frequent base: ", "green", end="")
print(freqbase)
