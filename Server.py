import socket

def iniciate_server():
    host = '127.0.0.1'
    puerto = 5000

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, puerto))
    servidor_socket.listen(5)
    print(f"Servidor escuchando en {host}:{puerto}")

    while True:
        try:
            cliente_socket, direccion = servidor_socket.accept()
            print(f"Conexión establecida con {direccion}")

            while True:
                try:
                    mensaje = cliente_socket.recv(1024).decode()
                    if not mensaje:
                        break
                    
                    print(f"Mensaje recibido del cliente: {mensaje}")

                    if mensaje.upper() == "DESCONEXION":
                        print("Cliente solicitó desconexión.")
                        cliente_socket.close()
                        print("Conexión cerrada con el cliente.")
                        break
                    elif mensaje.upper() == "TERMINAR":
                        print("Recibido comando para terminar el servidor.")
                        cliente_socket.close()
                        servidor_socket.close()
                    else:
                        respuesta = mensaje.upper()
                        cliente_socket.send(respuesta.encode())
                        print(f"Respuesta enviada al cliente: {respuesta}")
                except ConnectionAbortedError:
                    print("Conexión cerrada por el cliente.")
                    break
                except Exception as e:
                    print(f"Error al recibir datos del cliente: {e}")
                    cliente_socket.close()
                    break

        except Exception as e:
            print(f"Error al aceptar la conexión: {e}")
            continue
                
if __name__ == "__main__":
    iniciate_server()