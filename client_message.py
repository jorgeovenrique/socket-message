# number = input("Choisissez une proposition: ")
# number = int(number)

# if number == 0:
#     print("Première proposition")
# elif number == 1:
#     print("Seconde proposition")
# elif number == 2:
#     print("Troisième proposition")
# else:
#     print("Aucune proposition")

# message = input("Tapez votre message: ")
# message_title = input("Tapez le titre de votre message: ")
# message_dict = {message_title: message}
# print(message_dict)

import socket

server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_conn.connect(('127.0.0.1', 12800))
message_recv = server_conn.recv(1024)
print(message_recv.decode())


user_command = ""
while user_command != "exit":
    try:
        login
    except NameError:
        login = ""

    if login == "":
        # Demande à l'utilisateur de se connecter
        login_list = ["jorge", "jean", "jacques"]
        user_command = input("login: ")
        login = user_command
        if (login in login_list) == False:
            print("login incorrect, essayez à nouveau: ")
            login = ""
            continue

    # Impose un choix entre différentes propositions
    user_command = input(login + " Choisissez une proposition: ")
    action_number = user_command
    # Vérifie que le choix entré par l'utilisateur est bien un nombre entier
    try:
        action_number = int(action_number)
    except ValueError:
        print("proposition incorrect, essayez à nouveau:")
        action_number = ""
        continue
    
    # Effectue différentes opérations selon la proposition sélectionée
    if action_number == 0:
        user_command = input(login + " Tapez votre message: ")
        message = user_command
        user_command = input(login + " Tapez le titre de votre message: ")
        message_title = user_command
        user_command = input(login + " Tapez le nom du destinataire: ")
        recipient = user_command

        # Mémorise l'auteur du message, son message, son titre et son destinataire dans un dictionaire
        message_dict = {"author": login, "message": message, "message_title": message_title, "recipient": recipient}
        message_dict = str(message_dict)
        # Enregistre le dictionaire dans un document texte
        folder = open("client_message_list.txt", "a")
        folder.write("\n" + message_dict)
        folder.close
        # Envoie au serveur le dictionaire converti en octets
        if server_conn.fileno() == -1:
            print("Il n'y a pas de connexion, le message n'a donc pas pu être envoyé")

        server_conn.send(message_dict.encode("utf-8"))
        print(message_dict)

    elif action_number == 1:
        login = ""
        print("logout")

    elif action_number == 2:
        server_conn.send("close".encode("utf-8"))
        server_conn.close()
        print("vous avez été déconnecté")

    elif action_number == 3:
        # Teste si la connexion est effective
        if server_conn.fileno() != -1:
            print(server_conn)
            print("Le client est déjà connecté au serveur")
            continue
        
        # Reconnecte le client au serveur
        server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_conn.connect(('127.0.0.1', 12800))
        message_recv = server_conn.recv(1024)
        print(message_recv.decode())

    else:
        print("proposition incorrect, essayez à nouveau:")
    
# user_command = input(login + ": ")
