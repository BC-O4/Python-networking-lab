import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))
    
    message = "Hello from Python networking!"
    client_socket.send(message.encode())
    
    response = client_socket.recv(1024)
    print(f"Server echoed: {response.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    run_client()
