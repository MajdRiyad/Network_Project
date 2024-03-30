import socket

def client_program():
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 9955))

    student_id = input("Enter Student ID: ")  # Input for custom student ID
    client_socket.send(student_id.encode())  
    response = client_socket.recv(1024).decode()
    print("Response from server: " + response)

    client_socket.close()

if __name__ == '__main__':
    client_program()
