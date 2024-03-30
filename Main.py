from socket import *
serverPort = 9966  # Server will listen to this port
serverSocket = socket(AF_INET, SOCK_STREAM)  # TCP server creation
# Bind the socket to the server's address and port
serverSocket.bind(("", serverPort))
serverSocket.listen(1)  # Listen for incoming connections
print("The server is ready to receive")

# Keep the server running
while True:
    try:
        # Accept any incoming connection and retrieve the client's socket and address
        connectionSocket, addr = serverSocket.accept()
        # Receive data from the client and decode it
        sentence = connectionSocket.recv(2048).decode()
        print("addr:\n",)
        print("Sentence:", sentence)  # sentence == request

        request_parts = sentence.split()
        # bo5d kol el request message o befselhom 3an ba3ad o b5znhom f tuple
        print(request_parts)
        if len(request_parts) < 2:
            # Construct an HTTP response with a "Malformed Request" message
            response = "HTTP/1.1 400 Bad Request\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
            response += "<html><head><title>Error 400</title></head><body>"
            response += "<h1>HTTP/1.1 400 Bad Request</h1>"
            response += "<p>Your request is malformed and could not be understood by the server.</p>"
            response += "</body></html>"
        # Send the response to the client (browser)
            connectionSocket.send(response.encode())
            connectionSocket.close()
            continue
        # requested_path : bo5d el matloob mn el request o bkon el tarteeb ta3o el tane fel tuple
        requested_path = request_parts[1]

        # Check the requested path and send appropriate responses back to the client
        if requested_path == '/' or requested_path == '/index.html' or requested_path == '/main_en.html' or requested_path == '/en':
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
            with open("Project#1 Networks\main_en.html", "rb") as f:
                data = f.read()
            connectionSocket.send(response_header.encode())
            connectionSocket.send(data)
            print("\nResponse Header: \n", response_header)
            # print("data: \n", data)

        elif requested_path == '/ar':
           # print("Majd")
            response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
            with open("Project#1 Networks\main_ar.html", "rb") as f:
                data = f.read()
            connectionSocket.send(response_header.encode())
            connectionSocket.send(data)
            print("\nResponse Header: \n", response_header)

        # Redirect the client to external websites based on the path
        elif requested_path == '/cr':
            response_header = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://www.cornell.edu/\r\n\r\n"
            connectionSocket.send(response_header.encode())
            print("\nResponse Header: \n", response_header)
        elif requested_path == '/so':
            response_header = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://stackoverflow.com\r\n\r\n"
            connectionSocket.send(response_header.encode())
            print("\nResponse Header: \n", response_header)
        elif requested_path == '/rt':
            response_header = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://ritaj.birzeit.edu/\r\n\r\n"
            connectionSocket.send(response_header.encode())
            print("\nResponse Header: \n", response_header)

        # If the client requests a CSS file
        elif requested_path.endswith('.css'):
            try:
                with open(requested_path[1:], 'rb') as f:
                    data = f.read()
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/css; charset=utf-8\r\n\r\n"
                connectionSocket.send(response_header.encode())
                connectionSocket.send(data)
                print("\nResponse Header: \n", response_header)
            except FileNotFoundError:
                # Handle 404 for CSS file
                response_header = "HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(response_header.encode())
                print("\nResponse Header: \n", response_header)
                print("\nCSS file not found")

        # If the client requests a PNG file
        elif requested_path.endswith('.png'):
            try:
                s= r"Project#1 Networks{}{}".format("\\",requested_path[1:])
                print(s)
                with open(s, 'rb') as f:
                    data = f.read()
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: images\\r\n\r\n"
                connectionSocket.send(response_header.encode())
                connectionSocket.send(data)
                print("\nResponse Header: \n", response_header)
            except FileNotFoundError:
                # Handle 404 for PNG file
                response_header = "HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(response_header.encode())
                print("\nResponse Header: \n", response_header)
                print("\nPNG file not found")

        # If the client requests a JPG or JPEG file
        elif requested_path.endswith('.jpg'):
            try:
                s= r"Project#1 Networks{}{}".format("\\",requested_path[1:])
                with open(s, 'rb') as f:
                    data = f.read()
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: image\\r\n\r\n"
                connectionSocket.send(response_header.encode())
                connectionSocket.send(data)
                print("\nResponse Header: \n", response_header)
            except FileNotFoundError:
                # Handle 404 for JPG file
                response_header = "HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(response_header.encode())
                print("\nResponse Header: \n", response_header)
                print("JPG file not found")

        elif requested_path == '/local_file.html':
            try:
                with open("Project#1 Networks\local_file.html", "rb") as f:
                    data = f.read()
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
                connectionSocket.send(response_header.encode())
                connectionSocket.send(data)
                print("\nResponse Header: \n", response_header)
            except FileNotFoundError:
                response_header = "HTTP/1.1 404 Not Found\r\n\r\n"
                connectionSocket.send(response_header.encode())
                print("Local_file page not found\n")
                print("\nResponse Header: \n", response_header)

        else:
            # Handle 404 Not Found
                
                with open("Project#1 Networks\error.html", "rb") as f:
                    data = f.read()
                response_header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
                connectionSocket.send(response_header.encode())
                connectionSocket.send(data)
                print("\nResponse Header: \n", response_header)

        # Close the connection with the client because we are using TCP I guess
        connectionSocket.close()

    except OSError:
        print("IO error")
    else:
        print("OK for now")
        print("---------------------------------------------------")
