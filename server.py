import socket, sys

HOST = '127.0.0.1'
PORT = 50000
  # compteur de connexions actives
counter = 0
counterplayer = 0
players = {}
players["player1"] = {}
players["player2"] = {}

# 1) création du socket :
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) liaison du socket à une adresse précise :
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    # 3) Waiting the request of a client :
    print("Server ready, waiting for a request from client ...")
    mySocket.listen(2)

    if (counter == 0):
        # 4) Etablishing the connection :
        connexion, adresse = mySocket.accept()

        if (counterplayer == 0):
            players.update({"player1": {"address": adresse[0], "port": adresse[1], "socket": connexion}})
            players["player1"]["socket"].sendall(b'ok')
            counterplayer = 1
        elif (counterplayer == 1):
            if (players["player1"]["port"] != adresse[1]):
                players.update({"player2": {"address": adresse[0], "port": adresse[1], "socket": connexion}})
                players["player2"]["socket"].sendall(b'ok')
                counter = 1
    elif (counter == 1):
        players["player1"]["socket"].sendall(b"connexion ok")
        players["player2"]["socket"].sendall(b"connexion ok")

