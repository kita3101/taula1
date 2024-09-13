import socket

def start_client(host='127.0.0.1', port=65432):
    """Inicia o cliente para enviar mensagens e receber respostas do servidor."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        while True:
            message = input("Digite sua mensagem (ou 'sair' para encerrar): ")
            client_socket.sendall(message.encode('utf-8'))
            
            if message.lower() == 'sair':
                print("Encerrando o cliente.")
                break
            
            data = client_socket.recv(1024)
            print(f"Resposta do servidor: {data.decode('utf-8')}")

if __name__ == "__main__":
    start_client()
