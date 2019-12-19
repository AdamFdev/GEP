import socket
import os

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind(('', 12500))
connexion_principale.listen(5)
connexion_avec_client, infos_connexion = connexion_principale.accept()

print(infos_connexion)
print(connexion_avec_client.send(b"Connexion Acceptee"))
msg = connexion_avec_client.send(b"Reception du msg serveur par C")

print(connexion_avec_client.recv(1024))


connexion_avec_client.close()
connexion_principale.close()

