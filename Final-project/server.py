import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json
from Seq1 import Seq

list_bases = ["A", "C", "G", "T"]

def client_get_species(endpoint):
    PORT = 8080
    SERVER = 'rest.ensembl.org'
    print(f"\nConnecting to server: {SERVER}:{PORT}\n")
    conn = http.client.HTTPConnection(SERVER, timeout=100)
    try:
        conn.request("GET", endpoint)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data = r1.read().decode("utf-8")
    data1 = json.loads(data)
    return data1


def html_file(color, title):
    return f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <title>{title}</title>
            </head>
            <body style="background-color: {color}">
            <h1>{title}</h1>
            </body></html>
            """

def list_species(limit, list):
    contents = {
        "Total number of species": 267,
        "Limit selected": limit,
        "List of species": list
    }
    species_dict  = json.dumps(contents)
    return species_dict


def karyotype_dic(list):
    contents = {"The names of the chromosomes are": list
    }
    karyotype_dict = json.dumps(contents)
    return karyotype_dict

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        path = self.requestline.split()[1]
        arguments = path.split('?')
        firts_argument = arguments[0]

        try:

            if firts_argument == "/":
                contents = Path("main-page.html").read_text()
                self.send_response(200)

            elif firts_argument == "/listSpecies":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 2:
                    parameter, json = second_argument.split("&")
                    third_argument = parameter.split("=")[1]
                    data = client_get_species("info/species?content-type=application/json")

                    if json == "json=1":
                        new_list = []
                        counter = 0
                        contents_1 = data["species"]
                        if int(third_argument) < 267:
                            for element in contents_1:
                                if counter < int(third_argument):
                                    new_list.append(element["display_name"])
                                    counter += 1
                            contents = list_species(third_argument, new_list)
                        elif third_argument == "":
                            for element in contents_1:
                                new_list.append(element["display_name"])
                                counter += 1
                            contents = list_species(third_argument, new_list)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)
                elif len(new_argument) == 1:

                    third_argument = second_argument.split("=")[1]
                    data = client_get_species("info/species?content-type=application/json")
                    species = data["species"]
                    contents = html_file("lightblue", "List of species")
                    contents += f"""<p>Total number of species is 267</p>"""
                    if third_argument == "":
                        contents += f""" <p>The limit you have selected is:{267} </p>
                                        <p>The names of the species are:</p>"""
                        for element in species:
                            contents += f"""<p> · {element["display_name"]} </p>"""
                    elif 267 >= int(third_argument):
                        contents += f""" <p>Total number of species is: 267 </p>
                                    <p>The limit you have selected is: {third_argument}</p>
                                    <p>The names of the species are:</p>"""
                        count = 0
                        for element in species:
                            if count < int(third_argument):
                                contents += f'''<p> · {element["display_name"]}</p>'''
                            count += 1
                    else:
                        contents += f"""<p>Total number of species is: 267 </p>
                                        <p>The limit you have selected is:{third_argument}</p>
                                        <p>The names of the species are:</p>"""
                        for element in species:
                            contents += f"""<p> · {element["display_name"]} </p>"""
                    self.send_response(200)
            elif firts_argument == "/karyotype":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 2:
                    parameter, json = second_argument.split("&")
                    third_argument = parameter.split("=")[1]
                    data = client_get_species(f"/info/assembly/{third_argument}?content-type=application/json")

                    if json == "json=1":
                        contents_1 = data["karyotype"]
                        new_list = []
                        for element in contents_1:
                            new_list.append(element)
                        contents = karyotype_dic(new_list)
                        self.send_response(200)
                    else:
                        contents = Path('error.html').read_text()
                        self.send_response(404)
                elif len(new_argument) == 1:

                    third_argument = second_argument.split("=")[1]
                    species = client_get_species("info/assembly/" + third_argument +
                                             "?content-type=application/json")["karyotype"]
                    contents = html_file("pink", "Name of chromosomes:")
                    contents += f"""<p>The names of the chromosomes are: </p>"""
                    for element in species:
                        contents += f"""<p> · {element} </p>"""
                    self.send_response(200)
            elif firts_argument == "/chromosomeLength":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 3:
                    specie, chromosome, json = second_argument.split("&")
                    specie_1 = specie.split("=")[1]
                    chromo = chromosome.split("=")[1]
                    species = client_get_species("info/assembly/" + specie_1 +
                                             "?content-type=application/json")

                    if json == "json=1":
                        contents = species["top_level_region"]
                        self.send_response(200)
                    else:
                        info = species["top_level_region"]
                        contents = html_file("plum", "Chromosome length")
                        contents += "<h1> CHROMOSOME LENGTH </h1>"
                        for chromosome in info:
                            if chromosome["coord_system"] == "chromosome":
                                if chromosome["name"] == chromo:
                                    c_lenght = chromosome['length']
                                    contents += f"<p>The length of the chromosome {chromo} is: {c_lenght}</p>"
                        self.send_response(200)
                elif len(new_argument) == 2:
                    specie, chromosome = second_argument.split("&")
                    specie_1 = specie.split("=")[1]
                    chromo = chromosome.split("=")[1]
                    species = client_get_species("info/assembly/" + specie_1 +
                                             "?content-type=application/json")
                    info = species["top_level_region"]
                    contents = html_file("plum", "Chromosome length")
                    for element in info:
                        if element["coord_system"] == "chromosome":
                            if element["name"] == chromo:
                                contents += f"""<p> The length of the chromosome is: {element["length"]} </p>"""
                    self.send_response(200)
            elif firts_argument == "/geneSeq":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 2:
                    parameter, json = second_argument.split("&")
                    gene = parameter.split("=")[1]
                    id_gen = client_get_species(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = client_get_species(f"""/sequence/id/{id_gen}?content-type=application/json""")
                    if json == "json=1":
                        contents = data
                        self.send_response(200)
                    else:
                        contents = html_file("aquamarine", "Sequence of a human gene")
                        contents += f'<p> The sequence of gene {gene} is: </p>'
                        contents += f'<textarea rows = "100" "cols = 500"> {data["seq"]} </textarea>'
                        self.send_response(200)
                elif len(new_argument) == 1:
                    gene = second_argument.split("=")[1]
                    id_gen = client_get_species(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = client_get_species(f"""/sequence/id/{id_gen}?content-type=application/json""")
                    contents = html_file("aquamarine", "Sequence of a human gene")
                    contents += f'<p> The sequence of gene {gene} is: </p>'
                    contents += f'<textarea rows = "100" "cols = 500"> {data["seq"]} </textarea>'
                    self.send_response(200)
            elif firts_argument == "/geneInfo":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 2:
                    parameter, json = second_argument.split("&")
                    gene = parameter.split("=")[1]
                    id_gen = client_get_species(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = client_get_species(f"""/lookup/id/{id_gen}?content-type=application/json""")
                    if json == "json=1":
                        contents = data
                        self.send_response(200)
                    else:
                        contents = html_file("palevioletred", "Information of a human gene")
                        contents += f'<p> The gene is on chromosome {data["seq_region_name"]} </p>'
                        contents += f'<p> The start of the gene is: {data["start"]} </p>'
                        contents += f'<p> The end of the gene is: {data["end"]}</p>'
                        contents += f'<p> The length of the gene is: {data["end"] - data["start"]}</p>'
                        contents += f'<p> The identification of the gene is: {id_gen}</p>'
                        self.send_response(200)
                elif len(new_argument) == 1:
                    gene = second_argument.split("=")[1]
                    id_gen = \
                    client_get_species(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = client_get_species(f"""/lookup/id/{id_gen}?content-type=application/json""")
                    contents = html_file("palevioletred", "Information of a human gene")
                    contents += f'<p> The gene is on chromosome {data["seq_region_name"]} </p>'
                    contents += f'<p> The start of the gene is: {data["start"]} </p>'
                    contents += f'<p> The end of the gene is: {data["end"]}</p>'
                    contents += f'<p> The length of the gene is: {data["end"] - data["start"]}</p>'
                    contents += f'<p> The identification of the gene is: {id_gen}</p>'
                    self.send_response(200)
            elif firts_argument == "/geneCalc":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 2:
                    parameter, json = second_argument.split("&")
                    gene = parameter.split("=")[1]
                    id_gen = client_get_species(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = client_get_species(f"""/sequence/id/{id_gen}?content-type=application/json""")
                    if json == "json=1":
                        contents = data
                        self.send_response(200)
                    else:
                        sequence = data["seq"]
                        gene_seq = Seq(sequence)
                        contents = html_file("thistle", "Length and percentage of basis of the gene")
                        contents += f"The total lenght of the sequence is: {gene_seq.len()}"
                        for element in list_bases:
                            contents += f"<p>Base {element}: Percentage: ({gene_seq.count_base(element)[1]}%)</p>"
                            self.send_response(200)
                elif len(new_argument) == 1:
                    self.send_response(200)
                    gene = second_argument.split("=")[1]
                    id_gen = \
                    client_get_species(f"""/xrefs/symbol/homo_sapiens/{gene}?content-type=application/json""")[0]["id"]
                    data = client_get_species(f"""/sequence/id/{id_gen}?content-type=application/json""")
                    sequence = data["seq"]
                    gene_seq = Seq(sequence)
                    contents = html_file("thistle", "Length and percentage of basis of the gene")
                    contents += f"The total lenght of the sequence is: {gene_seq.len()}"
                    for element in list_bases:
                        contents += f"<p>Base {element}: Percentage: ({gene_seq.count_base(element)[1]}%)</p>"

            elif firts_argument == "/geneList":
                second_argument = arguments[1]
                new_argument = second_argument.split("&")
                if len(new_argument) == 4:
                    first, second, third, json = second_argument.split("&")
                    chromo = first.split("=")[1]
                    start = second.split("=")[1]
                    end = third.split("=")[1]
                    data = client_get_species("overlap/region/human/" + chromo + ":" + start + "-" + end +
                                              "?feature=gene;content-type=application/json")
                    if json == "json=1":
                        contents = data
                        self.send_response(200)
                    else:
                        contents = html_file("moccasin", "List of human genes")
                        for gene in data:
                            contents += f"<p> · {gene['external_name']} </p>"
                        self.send_response(200)
                elif len(new_argument) == 3:
                    self.send_response(200)
                    first, second, third = second_argument.split("&")
                    chromo = first.split("=")[1]
                    start = second.split("=")[1]
                    end = third.split("=")[1]
                    data = client_get_species("overlap/region/human/" + chromo + ":" + start + "-" + end +
                                              "?feature=gene;content-type=application/json")
                    contents = html_file("moccasin", "List of human genes")
                    for gene in data:
                        contents += f"<p> · {gene['external_name']} </p>"

            else:
                contents = Path('Error.html').read_text()
                self.send_response(404)


        except (KeyError, ValueError, IndexError, TypeError):
            contents = Path('Error.html').read_text()
            error_code = 400


        endpoints = ["","/", "/listSpecies", "/karyotype", "/chromosomeLength",
                    "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]

        #if firts_argument in endpoints:
            #if json == "json=1":
                #type = "application/json"
           # else:
                #type = "text/html"

        self.send_header('Content-Type', "text/html")
        self.send_header('Content-Length', len(str.encode(contents)))

        self.end_headers()

        self.wfile.write(str.encode(contents))

        return


Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
