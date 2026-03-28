import socket

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(1)
    print("Server listening on port 8888...")
    
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received: {data.decode()}")
        client_socket.send(data)  # Echo back
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    run_server()
