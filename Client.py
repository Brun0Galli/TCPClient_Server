import socket

def iniciate_client():
    host = '127.0.0.1'
    port = 5000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Conectando a {host}:{port}")
    
    while True:
        message = input("Ingresa un mensaje (o DESCONEXION para salir): ")
        
        client_socket.send(message.encode())
        
        if message.upper() == "DESCONEXION":
            print("Desconectando del servidor...")
            client_socket.close()
            print("Conexión cerrada.")
            break
        
        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
        
if __name__ == "__main__":
    iniciate_client()