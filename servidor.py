import socket

def handle_message(message):
    """Processa a mensagem recebida e retorna uma resposta personalizada."""
    if "olá" in message.lower():
        return "Olá! Como posso ajudar você hoje?"
    elif "ajuda" in message.lower():
        return "Claro, estou aqui para ajudar. O que você precisa?"
    elif "sair" in message.lower():
        return "Adeus! Tenha um bom dia!"
    else:
        return "Desculpe, não entendi a sua mensagem."

def start_server(host='127.0.0.1', port=65432):
    """Inicia o servidor para receber e responder mensagens dos clientes."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Servidor ouvindo em {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    message = data.decode('utf-8')
                    print(f"Recebido: {message}")
                    
                    response = handle_message(message)
                    conn.sendall(response.encode('utf-8'))

                    if "sair" in message.lower():
                        print("Encerrando a conexão.")
                        break

if __name__ == "__main__":
    start_server()
