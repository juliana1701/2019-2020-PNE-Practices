import http.client
import json

server = 'rest.ensembl.org'
endpoint = '/info/ping'
params = '?content-type=application/json'
URL = server + endpoint + params

print(f"\nConnecting to server: {server}")

conn = http.client.HTTPConnection(server)

try:
    conn.request("GET", endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

response = json.loads(data1)

if response["ping"] == 1:
    print("PING OK! The database is running!")
