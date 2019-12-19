import socket


connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect(('localhost', 12500))

print(connexion_avec_serveur.recv(1024))

connexion_avec_serveur.send(b"Reception du message clien par S")

print(connexion_avec_serveur.recv(1024))

connexion_avec_serveur.close()