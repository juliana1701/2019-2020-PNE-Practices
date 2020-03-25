import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080
folder = "../Session-04/"

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
list_number = ["ACCGT\n", "ACTGA\n", "CTA\n", "TGCA\n", "TTA\n"]


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
            contents = Path("form-4.html").read_text()
            error_code = 200

        elif firts_argument == "/ping":
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <h1>PING OK! </h1>
                        <body>
                        <p>The SEQ2 server is running</p>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            error_code = 200
        elif firts_argument == "/get":
            second_argument = arguments[1].split("=")[1]
            value = int(second_argument)
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <h1>Sequence number {value} </h1>
                        <body>
                        <p>{list_number[value]}</p>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            error_code = 200
        elif firts_argument == "/gene":
            second_argument = arguments[1].split("=")[1]
            gene = Seq()
            sequence = gene.read_fasta(folder + second_argument + ".txt")
            contents = f"""
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="utf-8">
                            <title>RESULT</title>
                        </head>
                        <h1>Gene: {second_argument} </h1>
                        <body>
                        <textarea readonly rows="20" cols="80"> {sequence} </textarea>
                        <br>
                        <a href="/">Main page</a>
                        </body></html>
                        """
            error_code = 200
        elif firts_argument == "/operation":
            second_argument = arguments[1].split("&")[0]
            third_argument = arguments[1].split("&")[1]
            sequence = second_argument.split("=")[1]
            seq1 = Seq(sequence)
            operation = third_argument.split("=")[1]
            if operation == "info":
                sl = seq1.len()
                count_a = seq1.count_base('A')[0]
                percent_a = seq1.count_base('A')[1]
                count_c = seq1.count_base('C')[0]
                percent_c = seq1.count_base('C')[1]
                count_g = seq1.count_base('G')[0]
                percent_g = seq1.count_base('G')[1]
                count_t = seq1.count_base('T')[0]
                percent_t = seq1.count_base('T')[1]

                result = f"""
                               <p>Total length: {sl}</p>
                               <p>A: {count_a} ({percent_a}%)</p>
                               <p>C: {count_c} ({percent_c}%)</p>
                               <p>G: {count_g} ({percent_g}%)</p>
                               <p>T: {count_t} ({percent_t}%)</p>"""
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <h2>Sequence</h2>
                            <body>
                            {sequence}
                            <br>
                             <h2>Operation:</h2>
                            {operation}
                            <br>
                            <h2>Result:</h2>
                            {result}
                            <br>
                            <a href="/">Main page</a>
                            </body></html>
                        """
            elif operation == "Comp":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <h2>Sequence</h2>
                            <body>
                            {sequence}
                            <br>
                             <h2>Operation:</h2>
                            {operation}
                            <br>
                            <h2>Result:</h2>
                            {seq1.complement()}
                            <a href="/">Main page</a>
                            </body></html>
                        """
            elif operation == "Rev":
                contents = f"""
                            <!DOCTYPE html>
                            <html lang="en">
                            <head>
                                <meta charset="utf-8">
                                <title>RESULT</title>
                            </head>
                            <h2>Sequence</h2>
                            <body>
                            {sequence}
                            <br>
                             <h2>Operation:</h2>
                            {operation}
                            <br>
                            <h2>Result:</h2>
                            {seq1.reverse()}
                            <br>
                            <a href="/">Main page</a>
                            </body></html>
                        """
            error_code = 200
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
