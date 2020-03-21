import http.server
import socketserver
import termcolor
import pathlib

# Define the Server's port
PORT = 8080


def read(filename):
    # -- Open and read the file
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


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

        # IN this simple server version:
        # We are NOT processing the client's request
        # It is a happy server: It always returns a message saying
        # that everything is ok

        request = self.requestline.split(" ")
        folder = "../P4/"
        folder2 ="../Session-14/"

        # Message to send back to the clinet
        if request[1] == " /" or request[1] == "/index.html":
            filename = "index.html"
            contents = read(folder2 + filename)
            self.send_response(200)
        else:
            filename = "Error.html"
            contents = read(folder + filename)
            self.send_response(404)

        status_line = "HTTP/1.1 200 OK\n"

        # Define the content-type header:
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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
