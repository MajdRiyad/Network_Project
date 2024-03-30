
import socket
import time
import os

def lock_screen():
    os.system('rundll32.exe user32.dll, LockWorkStation')

def server_program():
    valid_ids = ["1201462", "1202923", "1193191"]  # Valid student IDs
    server_socket = socket.socket()  
    server_socket.bind(('0.0.0.0', 9955))

    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()
        print("Connection from: " + str(address))
        print("sever is waiting for ID from client")
        data = conn.recv(1024).decode()
        if data in valid_ids:
            print("Valid ID received. OS will lock screen after 10 seconds")
            conn.send("Server will lock screen after 10 seconds".encode())
            time.sleep(10)
            lock_screen()
        else:
            print(f"Invalid ID received: {data}. No action taken.")
            conn.send("Invalid ID. No action taken.".encode())
        conn.close()

if __name__ == '__main__':
    server_program()
