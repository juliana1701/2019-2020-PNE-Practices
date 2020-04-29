import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
import json

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


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        path = self.requestline.split()[1]
        arguments = path.split('?')
        firts_argument = arguments[0]

        if firts_argument == "/":
            contents = Path("main-page.html").read_text()
            error_code = 200

        elif firts_argument == "/listSpecies":
            second_argument = arguments[1]
            third_argument = second_argument.split("=")[1]
            species = client_get_species("info/species?content-type=application/json")["species"]
            if third_argument == "":
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightblue">
                                <p>Total number of species is: 267 </p>
                                <p>The limit you have selected is:{267} </p>
                                <p>The names of the species are:</p>
                                </body></html>
                                """
                error_code = 200
                for element in species:
                    contents += f"""<p> · {element["common_name"]} </p>"""
            elif 267 >= int(third_argument):
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>List of species</title>
                            </head>
                            <body style="background-color: lightblue">
                            <p>Total number of species is: 267 </p>
                            <p>The limit you have selected is: 267 </p>
                            <p>The names of the species are:</p>
                            </body></html>
                            """
                error_code = 200
                count = 0
                for element in species:
                    if count < int(third_argument):
                        contents += f'''<p> · {element["common_name"]}</p>'''
                    count += 1
            else:
                contents = f"""
                                <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="utf-8">
                                    <title>List of species</title>
                                </head>
                                <body style="background-color: lightblue">
                                <p>Total number of species is: 267 </p>
                                <p>The limit you have selected is:{third_argument}</p>
                                <p>The names of the species are:</p>
                                </body></html>
                                """
                error_code = 200
                for element in species:
                    contents += f"""<p> · {element["common_name"]} </p>"""
        else:
            contents = Path('Error.html').read_text()
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
