import socket
from cryptography.fernet import Fernet

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
    while i < 10:
        # Permet de sortir de la boucle si la connexion est interrompue coté client
        if message_recv == "close":
            break
        elif message_recv == "stop":
            break
        message_recv = client_conn.recv(1024)
        
        # Détecte si le message est chiffré
        if message_recv.decode()[0:7] == "encrypt":
            print("Déchiffrement du message reçu...")
            # Récupère la clé stocké dans key_file.txt
            key_file = open("key.txt", "r")
            key_file_content = key_file.read()
            key_file.close()

            fernet = Fernet(key_file_content)
            # Soustrait le préfix en commencant au 8ème caractère(l'indice part de 0, soit le caractère "7") c'est à dire après le mot "encrypt"
            message_recv = message_recv[7:]
            print(message_recv)

            # Décrypte le message
            message_recv = fernet.decrypt(message_recv)

        # Converti le message reçu en chaine de caratères    
        message_recv = message_recv.decode()

        # Filtre les messages, si ce sont "close" ou "stop" qui sont envoyés il est inutile de les enregistrer
        if message_recv != "close" and message_recv != "stop":
            # Enregistre le message reçu dans le document server_message_list
            message_file = open("server_message_list.txt", "a")
            message_file.write("\n"+message_recv)
            message_file.close
            print("message enregistré")

        print(message_recv)
        i+=1
        print(i)
    
    client_conn.close()