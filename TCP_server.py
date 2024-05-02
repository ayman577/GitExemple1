import socket
import threading

ip = '0.0.0.0'
port = 9998

def main() : 
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)
    print(f"listening on {ip}:{port}....")
    while True : 
        data, addr = server.accept()
        print(f"accepted connection for {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(data,))
        client_handler.start()

def handle_client(client_socket) : 
    with client_socket as sock : 
        request = sock.recv(4096)
        print(f"Received: {request.decode()}")
        sock.send(b"ACK")

if __name__ == '__main__':
    main()