import socket

message_recv = ""
while message_recv != "stop":
    socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conn.bind(('127.0.0.1', 12800))
    socket_conn.listen(5)
    client_conn, client_addr = socket_conn.accept()
    print('Connected by', client_addr)
    message_conn_to_client = "La connexion avec le serveur a bien été établie"
    bytes_to_send = client_conn.send(message_conn_to_client.encode("utf-8"))
    print(bytes_to_send)
    
    # Reset la variable "message_recv" après une reconnexion
    message_recv = ""
    # Limite les itérations à 10 pour éviter une boucle infinie
    i = 0
    while (message_recv != "close") and (i < 10):
        if message_recv == "stop":
            break
        message_recv = client_conn.recv(1024)
        message_recv = message_recv.decode()

        if message_recv != "close" and message_recv != "stop":
            # Enregistre le message reçu dans le document server_message_list
            folder = open("server_message_list.txt", "a")
            folder.write("\n"+message_recv)
            folder.close
            print("message enregistré")

        print(message_recv)
        i+=1
        print(i)
    
    client_conn.close()